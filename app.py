import streamlit as st
import pandas as pd
from src.pipeline.chat_pipeline import ChatPipeline

# Page config
st.set_page_config(
    page_title="NL2SQL AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 NL2SQL AI Assistant")
st.caption("Ask questions in natural language → Get SQL + Charts")

# Initialize pipeline
if "pipeline" not in st.session_state:
    st.session_state.pipeline = ChatPipeline()

if "history" not in st.session_state:
    st.session_state.history = []

# Input box
question = st.text_input("💬 Ask your question:")

col1, col2 = st.columns([1, 5])

with col1:
    run_btn = st.button("Run")

# Run query
if run_btn and question:
    response = st.session_state.pipeline.run(question)

    st.session_state.history.append({
        "question": question,
        "response": response
    })

# Display history
for item in reversed(st.session_state.history):
    st.markdown("---")
    st.subheader(f"🧑 {item['question']}")

    response = item["response"]

    if response["status"] == "success":
        # SQL
        st.markdown("### 📊 Generated SQL")
        st.code(response["query"], language="sql")

        # Data
        result = response["result"]
        df = pd.DataFrame(result["rows"], columns=result["columns"])

        st.markdown("### 📈 Result Table")
        st.dataframe(df, use_container_width=True)

        # Chart
        st.markdown("### 📉 Visualization")

        if df.shape[1] == 2:
            x_col = df.columns[0]
            y_col = df.columns[1]

            st.bar_chart(df.set_index(x_col))

        elif df.shape[1] == 1:
            st.metric(label=df.columns[0], value=df.iloc[0, 0])

        else:
            st.info("Chart not available for this query")

    elif response["status"] == "text_only":
        st.write(response["message"])

    else:
        st.error(response["error"])
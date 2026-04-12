# NL2SQL_PROJECT

# 🧠 NL2SQL AI Agent (Custom LLM-Based System)

An advanced AI-powered system that converts natural language into SQL queries using Gemini and executes them on a database with built-in validation and visualization.

---

## 🚀 Features

* 💬 Natural Language → SQL (powered by Gemini)
* 🛡️ SQL Validation (only safe queries allowed)
* ⚙️ Query Execution Engine
* 📊 Chart Generation (data visualization)
* 🧱 Modular Architecture (production-ready structure)
* 🧪 Multiple Test Modules
* 🗄️ SQLite Database Integration

---

## 🧠 How It Works

1. User enters a query in plain English
2. Gemini generates SQL
3. SQL Validator ensures safety
4. Query Executor runs it on database
5. Results are returned (table/chart)

---

## 🏗️ Project Structure

```
nl2sql_project/
│
├── app.py                      # Streamlit UI
├── main.py                     # CLI entry point
│
├── config/
│   └── config.py               # Configuration settings
│
├── database/
│   ├── db_connection.py        # DB connection handler
│   ├── db_seed.py              # Seed sample data
│   ├── db_setup.py             # Database setup
│
├── logs/                       # Application logs
│
├── src/
│   ├── api/                    # (Future API layer)
│   │
│   ├── components/
│   │   ├── chart_generator.py  # Data visualization
│   │   ├── query_executor.py   # Executes SQL queries
│   │   ├── sql_validator.py    # Validates SQL safety
│   │   ├── ai_agent.py         # Core NL2SQL agent logic
│   │
│   ├── pipeline/
│   │   └── chat_pipeline.py    # End-to-end pipeline
│   │
│   ├── utils/
│   │   ├── logger.py           # Logging utility
│   │   ├── helpers.py          # Helper functions
│   │   ├── exception.py        # Custom exceptions
│
├── tests/
│   ├── test_pipeline.py
│   ├── test_query_executor.py
│   ├── test_sql_validator.py
│   ├── test_ai_agent.py
│
├── clinic.db                   # SQLite database
├── setup_database.py           # Initialize DB
│
├── requirements.txt
├── RESULTS.md                  # Sample outputs/results
├── README.md
└── .env
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/nl2sql_project.git
cd nl2sql_project

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

### Run CLI

```bash
python main.py
```

### Run Streamlit UI

```bash
streamlit run app.py
```

---

## 🧪 Run Tests

```bash
python tests/test_pipeline.py
python tests/test_query_executor.py
python tests/test_sql_validator.py
python tests/test_ai_agent.py
```

---

## 🛡️ Security

* Only `SELECT` queries are allowed
* Prevents unsafe operations (DELETE, UPDATE, DROP)

---

## 📊 Example

**Input:**

```
Show total revenue by month
```

**Generated SQL:**

```sql
SELECT month, SUM(revenue)
FROM invoices
GROUP BY month;
```

---

## 🔥 Key Highlights

* Custom-built **LLM-powered NL2SQL agent**
* Modular, scalable architecture (industry-level)
* Built-in validation for safe query execution
* Ready for production extension (API, deployment)

---

## 🚀 Future Improvements

* 🌐 FastAPI backend
* 🧠 Smarter schema-aware prompting
* 🔁 Auto-retry for failed SQL
* 📈 Advanced dashboards
* ☁️ Deployment (Docker / AWS)

---



## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

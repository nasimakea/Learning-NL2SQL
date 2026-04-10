"# NL2SQL_PROJECT" 
# 🧠 NL2SQL AI Agent (Custom Vanna-like System)

An advanced AI-powered system that converts natural language into SQL queries using Gemini and executes them on a database with built-in validation, memory, and visualization.

---

## 🚀 Features

* 💬 Natural Language → SQL (powered by Gemini)
* 🛡️ SQL Validation (only safe queries allowed)
* ⚙️ Query Execution Engine
* 🧠 Query Memory (stores past interactions)
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
6. Query + SQL stored in memory

---

## 🏗️ Project Structure

```id="projstruct"
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
│   │   ├── memory.py           # Query memory storage
│   │   ├── query_executor.py   # Executes SQL queries
│   │   ├── sql_validator.py    # Validates SQL safety
│   │   ├── vanna_agent.py      # Core NL2SQL agent logic
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
│   ├── test_vanna.py
│
├── clinic.db                   # SQLite database
├── seed_memory.py              # Preload memory
├── setup_database.py           # Initialize DB
│
├── requirements.txt
├── RESULTS.md                  # Sample outputs/results
├── README.md
└── .env
```

---

## ⚙️ Installation

```bash id="install"
git clone https://github.com/your-username/nl2sql_project.git
cd nl2sql_project

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```id="env"
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

### Run CLI

```bash id="runcli"
python main.py
```

### Run Streamlit UI

```bash id="runui"
streamlit run app.py
```

---

## 🧪 Run Tests

```bash id="tests"
python test_pipeline.py
python test_query_executor.py
python test_sql_validator.py
python test_vanna.py
```

---

## 🛡️ Security

* Only `SELECT` queries are allowed
* Prevents unsafe operations (DELETE, UPDATE, DROP)

---

## 📊 Example

**Input:**

```id="input"
Show total revenue by month
```

**Generated SQL:**

```sql id="sql"
SELECT month, SUM(revenue)
FROM invoices
GROUP BY month;
```

---

## 🔥 Key Highlights

* Custom-built **Vanna-like agent** (not using framework)
* Modular, scalable architecture (industry-level)
* Built-in validation + memory (advanced feature)
* Ready for production extension (API, deployment)

---

## 🚀 Future Improvements

* 🌐 FastAPI backend
* 🧠 Smarter schema-aware prompting
* 🔁 Auto-retry for failed SQL
* 📈 Advanced dashboards
* ☁️ Deployment (Docker / AWS)

---

## 👨‍💻 Author

Nasim

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

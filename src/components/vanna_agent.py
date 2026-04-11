import google.generativeai as genai
from config.config import Config
from src.utils.logger import logging

logger = logging.getLogger(__name__)


class SimpleSQLAgent:
    def __init__(self):
        logger.info("Initializing Gemini model...")
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def ask(self, question: str) -> str:

        schema = """
        Tables:

        patients(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            date_of_birth DATE,
            gender TEXT,
            city TEXT,
            registered_date DATE
        )

        doctors(
            id INTEGER PRIMARY KEY,
            name TEXT,
            specialization TEXT,
            department TEXT,
            phone TEXT
        )

        appointments(
            id INTEGER PRIMARY KEY,
            patient_id INTEGER,
            doctor_id INTEGER,
            appointment_date DATETIME,
            status TEXT,
            notes TEXT
        )

        treatments(
            id INTEGER PRIMARY KEY,
            appointment_id INTEGER,
            treatment_name TEXT,
            cost REAL,
            duration_minutes INTEGER
        )

        invoices(
            id INTEGER PRIMARY KEY,
            patient_id INTEGER,
            invoice_date DATE,
            total_amount REAL,
            paid_amount REAL,
            status TEXT
        )

        Relationships:
        - appointments.patient_id -> patients.id
        - appointments.doctor_id -> doctors.id
        - treatments.appointment_id -> appointments.id
        - invoices.patient_id -> patients.id
        """

        prompt = f"""
        You are an expert SQL generator for a healthcare database.

        Database Schema:
        {schema}

        Instructions:
        - Use ONLY the tables and columns provided
        - Use proper JOINs when needed
        - Prefer explicit JOIN syntax (INNER JOIN, LEFT JOIN)
        - Use meaningful aliases (p, d, a, t, i)
        - Always handle NULLs if relevant
        - Use aggregation (COUNT, SUM, AVG) when required
        - Use WHERE clauses properly
        - SQLite syntax only

        Output Rules:
        - Return ONLY SQL
        - Wrap SQL inside ```sql``` block
        - Do NOT explain anything

        Examples:
        Q: Total number of patients
        A:
        ```sql
        SELECT COUNT(*) FROM patients;
        ```

        Q: List appointments with doctor names
        A:
        ```sql
        SELECT a.id, d.name, a.appointment_date
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.id;
        ```

        Question:
        {question}
        """

        response = self.model.generate_content(prompt)
        return response.text.strip()


def get_vanna_agent():
    logger.info("Using custom Gemini SQL Agent (No Vanna)")
    return SimpleSQLAgent()
import google.generativeai as genai
from config.config import Config
from src.utils.logger import logging

logger = logging.getLogger(__name__)

class SimpleSQLAgent:
    def __init__(self):
        logger.info("Initializing Gemini model...")
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def ask(self, question: str):
        schema = """
        Tables:
        patients(id, first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)

        appointments(id, patient_id, doctor_id, appointment_date, status, notes)
        doctors(id, name, specialization, department, phone)
        """

        prompt = f"""
        You are an expert SQL generator.

        Database Schema:
        {schema}

        Rules:
        - Use only given tables
        - Return ONLY SQL in ```sql``` block
        - SQLite syntax

        Question:
        {question}
        """

        response = self.model.generate_content(prompt)
        return response.text


def get_vanna_agent():
    logger.info("Using custom Gemini SQL Agent (No Vanna)")
    return SimpleSQLAgent()
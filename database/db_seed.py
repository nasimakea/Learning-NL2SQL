# database/db_seed.py

import random
from datetime import datetime, timedelta
from faker import Faker

from database.db_connection import get_db_connection

fake = Faker()

SPECIALIZATIONS = [
    "Dermatology", "Cardiology", "Orthopedics", "General", "Pediatrics"
]

CITIES = [
    "Delhi", "Mumbai", "Bangalore", "Chandigarh", "Hyderabad",
    "Pune", "Kolkata", "Jaipur", "Lucknow", "Ahmedabad"
]

APPOINTMENT_STATUS = ["Scheduled", "Completed", "Cancelled", "No-Show"]
INVOICE_STATUS = ["Paid", "Pending", "Overdue"]




def random_date_within_last_year():
    days_ago = random.randint(0, 365)
    return datetime.now() - timedelta(days=days_ago)




def insert_doctors(conn):
    cursor = conn.cursor()

    doctors = []
    for _ in range(15):
        specialization = random.choice(SPECIALIZATIONS)
        doctors.append((
            fake.name(),
            specialization,
            specialization + " Department",
            fake.phone_number()
        ))

    cursor.executemany("""
        INSERT INTO doctors (name, specialization, department, phone)
        VALUES (?, ?, ?, ?)
    """, doctors)

    return len(doctors)




def insert_patients(conn):
    cursor = conn.cursor()

    patients = []
    for _ in range(200):
        patients.append((
            fake.first_name(),
            fake.last_name(),
            fake.email() if random.random() > 0.2 else None,
            fake.phone_number() if random.random() > 0.2 else None,
            fake.date_of_birth(minimum_age=1, maximum_age=90),
            random.choice(["M", "F"]),
            random.choice(CITIES),
            random_date_within_last_year().date()
        ))

    cursor.executemany("""
        INSERT INTO patients (
            first_name, last_name, email, phone,
            date_of_birth, gender, city, registered_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, patients)

    return len(patients)




def insert_appointments(conn):
    cursor = conn.cursor()

    # get ids
    patient_ids = [row["id"] for row in cursor.execute("SELECT id FROM patients")]
    doctor_ids = [row["id"] for row in cursor.execute("SELECT id FROM doctors")]

    appointments = []

    for _ in range(500):
        appointments.append((
            random.choice(patient_ids),
            random.choice(doctor_ids),
            random_date_within_last_year(),
            random.choice(APPOINTMENT_STATUS),
            fake.sentence() if random.random() > 0.3 else None
        ))

    cursor.executemany("""
        INSERT INTO appointments (
            patient_id, doctor_id, appointment_date, status, notes
        )
        VALUES (?, ?, ?, ?, ?)
    """, appointments)

    return len(appointments)




def insert_treatments(conn):
    cursor = conn.cursor()

    appointment_ids = [
        row["id"]
        for row in cursor.execute(
            "SELECT id FROM appointments WHERE status='Completed'"
        )
    ]

    treatments = []

    for _ in range(min(350, len(appointment_ids))):
        treatments.append((
            random.choice(appointment_ids),
            fake.word().capitalize() + " Treatment",
            round(random.uniform(50, 5000), 2),
            random.randint(10, 120)
        ))

    cursor.executemany("""
        INSERT INTO treatments (
            appointment_id, treatment_name, cost, duration_minutes
        )
        VALUES (?, ?, ?, ?)
    """, treatments)

    return len(treatments)




def insert_invoices(conn):
    cursor = conn.cursor()

    patient_ids = [row["id"] for row in cursor.execute("SELECT id FROM patients")]

    invoices = []

    for _ in range(300):
        total = round(random.uniform(100, 5000), 2)
        paid = total if random.random() > 0.4 else round(random.uniform(0, total), 2)

        status = (
            "Paid" if paid == total else random.choice(["Pending", "Overdue"])
        )

        invoices.append((
            random.choice(patient_ids),
            random_date_within_last_year().date(),
            total,
            paid,
            status
        ))

    cursor.executemany("""
        INSERT INTO invoices (
            patient_id, invoice_date, total_amount, paid_amount, status
        )
        VALUES (?, ?, ?, ?, ?)
    """, invoices)

    return len(invoices)




def seed_database():
    with get_db_connection() as conn:
        print("🌱 Seeding database...")

        doctors = insert_doctors(conn)
        patients = insert_patients(conn)
        appointments = insert_appointments(conn)
        treatments = insert_treatments(conn)
        invoices = insert_invoices(conn)

        conn.commit()

        print(f"Created {doctors} doctors")
        print(f"Created {patients} patients")
        print(f"Created {appointments} appointments")
        print(f"Created {treatments} treatments")
        print(f"Created {invoices} invoices")


if __name__ == "__main__":
    seed_database()
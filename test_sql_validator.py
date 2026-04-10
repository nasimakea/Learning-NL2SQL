# test_sql_validator.py

from src.components.sql_validator import SQLValidator

validator = SQLValidator()

# ✅ valid query
query1 = "SELECT * FROM patients LIMIT 5"

# ❌ invalid query
query2 = "DROP TABLE patients"

print("Valid Test:", validator.validate(query1))

try:
    validator.validate(query2)
except Exception as e:
    print("Invalid Test:", e)
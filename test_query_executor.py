# test_query_executor.py

from src.components.query_executor import QueryExecutor

executor = QueryExecutor()

query = "SELECT * FROM patients LIMIT 5"

result = executor.execute_query(query)

print(result)
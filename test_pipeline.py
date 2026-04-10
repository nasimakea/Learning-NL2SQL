# test_pipeline.py

from src.pipeline.chat_pipeline import ChatPipeline

pipeline = ChatPipeline()

# ✅ valid query
query = "SELECT first_name, city FROM patients LIMIT 5"

result = pipeline.run(query)

print(result)
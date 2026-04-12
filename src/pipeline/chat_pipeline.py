import re
import sys
from src.utils.logger import logging
from src.utils.exception import CustomException

from src.components.ai_agent import get_sql_agent
from src.components.sql_validator import SQLValidator
from src.components.query_executor import QueryExecutor
from src.components.chart_generator import ChartGenerator

logger = logging.getLogger(__name__)

class ChatPipeline:
    def __init__(self):
        try:
            logger.info("Initializing ChatPipeline components...")
            self.vn = get_sql_agent()   
            self.validator = SQLValidator()
            self.executor = QueryExecutor()
            self.chart_generator = ChartGenerator()
            logger.info("All components initialized.")
        except Exception as e:
            logger.error("Initialization failed.")
            raise CustomException(e, sys)

    def run(self, question: str):
        sql_query = None

        try:
            logger.info(f"Received question: {question}")

            # 1️⃣ Ask Vanna
            response = self.vn.ask(question)
            logger.info(f"Raw response: {response}")

            # 2️⃣ Extract SQL
            match = re.search(r"```sql(.*?)```", str(response), re.DOTALL)

            if match:
                sql_query = match.group(1).strip()
                logger.info(f"Extracted SQL: {sql_query}")

                # 3️⃣ Validate
                self.validator.validate(sql_query)

                # 4️⃣ Execute
                result = self.executor.execute_query(sql_query)
                self.chart_generator.generate_chart(result)

                return {
                    "query": sql_query,
                    "result": result,
                    "status": "success"
                }

            # 5️⃣ Fallback
            return {
                "message": str(response),
                "status": "text_only"
            }

        except CustomException as ce:
            logger.error(f"Custom Error: {str(ce)}")
            return {
                "error": str(ce),
                "status": "failed",
                "query": sql_query
            }

        except Exception as e:
            error_msg = CustomException(e, sys)
            logger.error(f"Unexpected Pipeline Error: {str(error_msg)}")
            return {
                "error": str(error_msg),
                "status": "error"
            }
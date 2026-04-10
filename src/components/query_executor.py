import sys
from database.db_connection import get_db_connection
from src.utils.exception import CustomException
from src.utils.logger import logging

# Initialize logger
logger = logging.getLogger(__name__)

class QueryExecutor:
    def __init__(self):
        logger.info("QueryExecutor initialized.")

    def execute_query(self, query: str):
        """
        Execute a SELECT query safely and return results.
        """
        try:
            logger.info(f"Preparing to execute query: {query}")
            
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Execute the query
                cursor.execute(query)
                rows = cursor.fetchall()
                
                # Extract column names from cursor description
                columns = [desc[0] for desc in cursor.description]
                
                # Convert rows to a list of lists
                data = [list(row) for row in rows]
                
                row_count = len(data)
                logger.info(f"Query execution successful. Retrieved {row_count} rows.")

                return {
                    "columns": columns,
                    "rows": data,
                    "row_count": row_count
                }

        except Exception as e:
            # Log the database-level error before raising the custom exception
            logger.error(f"Database execution error: {str(e)}")
            raise CustomException(e, sys)
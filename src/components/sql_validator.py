import re
import sys
from src.utils.logger import logging
from src.utils.exception import CustomException

# Initialize logger for this component
logger = logging.getLogger(__name__)

class SQLValidator:
    def __init__(self):
        # dangerous keywords
        self.forbidden_keywords = [
            "INSERT", "UPDATE", "DELETE", "DROP", "ALTER",
            "EXEC", "GRANT", "REVOKE", "SHUTDOWN"
        ]
        logger.info("SQLValidator initialized with restricted keyword list.")

    def validate(self, query: str):
        """
        Validate SQL query:
        - Only SELECT allowed
        - No dangerous keywords
        - No system tables
        """
        try:
            logger.info("Starting SQL validation process...")
            query_upper = query.upper().strip()

            # 1. Must start with SELECT
            if not query_upper.startswith("SELECT"):
                error_msg = "Only SELECT queries are allowed."
                logger.warning(f"Validation failed: {error_msg} | Query: {query}")
                raise ValueError(error_msg)

            # 2. Check forbidden keywords
            for keyword in self.forbidden_keywords:
                if re.search(rf"\b{keyword}\b", query_upper):
                    error_msg = f"Forbidden keyword detected: {keyword}"
                    logger.warning(f"Validation failed: {error_msg} | Query: {query}")
                    raise ValueError(error_msg)

            # 3. Block system tables
            if "SQLITE_MASTER" in query_upper:
                error_msg = "Access to system tables is not allowed."
                logger.warning(f"Validation failed: {error_msg} | Query: {query}")
                raise ValueError(error_msg)

            logger.info("SQL validation successful.")
            return True

        except Exception as e:
            # If it's a ValueError we raised, log it as a warning. 
            # If it's something unexpected, log it as an error.
            if not isinstance(e, ValueError):
                logger.error(f"Unexpected error during SQL validation: {str(e)}")
            
            raise CustomException(e, sys)
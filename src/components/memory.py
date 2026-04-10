import sys
import os
from vanna.chromadb import ChromaDB_VectorStore
from src.utils.logger import logging
from src.utils.exception import CustomException

logger = logging.getLogger(__name__)

class MyMemory(ChromaDB_VectorStore):
    def __init__(self):
        try:
            # path: where the 'brain' of your agent will be stored
            # This creates a folder named 'vanna_memory' in your project root
            config = {'path': os.path.join(os.getcwd(), "vanna_memory")}
            
            logger.info(f"Initializing ChromaDB Vector Store at: {config['path']}")
            
            super().__init__(config=config)
            
            logger.info("Memory component (ChromaDB) successfully initialized.")
            
        except Exception as e:
            logger.error("Failed to initialize Memory component.")
            raise CustomException(e, sys)
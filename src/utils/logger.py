import logging
import os
from datetime import datetime

# Create a 'logs' directory in the current working directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Also enable console logging so you can see it in your terminal
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)
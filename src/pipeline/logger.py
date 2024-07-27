import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
try:
    os.makedirs(logs_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating directory {logs_dir}: {e}")
    raise

# Combine the directory and log file name to get the full path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
    logging.info("Logging has started")
    print(f"Logging to {LOG_FILE_PATH}")


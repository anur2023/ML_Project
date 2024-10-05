import logging
import os
from datetime import datetime

# Create log file name with timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Set up the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Check if the directory was successfully created
if os.path.isdir(logs_dir):
    LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE_NAME)

    # Configure logging
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d.%(name)s-%(levelname)s-%(message)s",
        level=logging.INFO 
    )

    # if __name__ == "__main__":
    #     logging.info("Logging has started.")

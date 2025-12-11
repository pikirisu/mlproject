import logging
import os
from datetime import datetime

LOG_FILE = datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".log"
logs_dir = os.path.join(os.getcwd(), "logs")


log_file_path = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
console_handler.setFormatter(console_format)

logging.getLogger().addHandler(console_handler)

logger = logging.getLogger(__name__)

# logger.info("Logging system initialized successfully.")    # Normal operation info
# logger.warning("This is a sample warning message.")        # Something unexpected but not fatal
# logger.error("This is a sample error message.")            # Something failed but program can continue

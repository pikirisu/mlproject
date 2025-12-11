import logging
import os
from datetime import datetime

# ---------------------------------------------------------
# STEP 1: Create a timestamped log file name
# ---------------------------------------------------------
# datetime.now()          → gets the current date & time
# strftime()              → formats it into a readable string format (DD_MM_YYYY_HH_MM_SS)
# Adding ".log"           → extension for log files
LOG_FILE = datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".log"

# ---------------------------------------------------------
# STEP 2: Create the full path for the log file
# ---------------------------------------------------------
# os.getcwd()             → gets the current working directory of the project
# "logs"                  → folder where all log files will be stored
# os.path.join()          → safely combines folder paths across OS (Windows/Linux/Mac)
logs_dir = os.path.join(os.getcwd(), "logs")

# ---------------------------------------------------------
# STEP 3: Ensure that the "logs" directory exists
# ---------------------------------------------------------
# os.makedirs()           → creates directory; if it already exists, no error is thrown
# exist_ok=True           → prevents crashing when folder already exists
os.makedirs(logs_dir, exist_ok=True)

# Full path for the log file including folder + timestamped name
log_file_path = os.path.join(logs_dir, LOG_FILE)

# ---------------------------------------------------------
# STEP 4: Configure the main logging system
# ---------------------------------------------------------
# logging.basicConfig() sets:
#   - filename   → where logs will be written
#   - format     → how each log entry should appear
#   - level      → the minimum level of messages to record
#
# Format used:
#   %(asctime)s  → timestamp of log
#   %(levelname)s→ INFO, WARNING, ERROR, DEBUG
#   %(name)s     → name of the module/logger
#   %(message)s  → the log message
logging.basicConfig(
    filename=log_file_path,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

# ---------------------------------------------------------
# STEP 5: Add Console Logging (so logs appear in terminal also)
# ---------------------------------------------------------
# StreamHandler()         → outputs logs to console
# setLevel()              → minimum level for console logs
# Formatter()             → format for console logs (separate from file logs if needed)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
console_handler.setFormatter(console_format)

# Add the console handler to the global logger
logging.getLogger().addHandler(console_handler)

# ---------------------------------------------------------
# STEP 6: Create a logger for this module/file
# ---------------------------------------------------------
# getLogger(__name__)     → best practice; identifies logs by module name
logger = logging.getLogger(__name__)

# ---------------------------------------------------------
# STEP 7: Example usage demonstrating different log levels
# ---------------------------------------------------------
logger.info("Logging system initialized successfully.")    # Normal operation info
logger.warning("This is a sample warning message.")        # Something unexpected but not fatal
logger.error("This is a sample error message.")            # Something failed but program can continue

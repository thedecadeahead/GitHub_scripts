import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Log to a file
log_filename = '/Users/james.richardson/Library/CloudStorage/OneDrive-Personal/Desktop/python/Stock-o-tron/logs/test_logging.log'
file_handler = logging.FileHandler(log_filename)
logger.addHandler(file_handler)

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.error("This is an error message.")

print("Logging test complete. Check the logs folder.")
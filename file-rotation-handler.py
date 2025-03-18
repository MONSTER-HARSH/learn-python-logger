import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=3)

# Configure logging
logging.basicConfig(
    handlers=[handler],
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Test log messages
for i in range(10000):  
    logging.info(f"Log entry {i}")


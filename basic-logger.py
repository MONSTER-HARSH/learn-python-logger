import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s") #log with format
logging.basicConfig(level=logging.DEBUG) #log without format

'''
Level	    Numeric Value   When to Use?
DEBUG	    10	            Detailed debugging info
INFO	    20	            General app flow info
WARNING	    30	            Something unexpected but not an error
ERROR	    40	            A function failed but app continues
CRITICAL	50	            Serious issue, app might crash
'''

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")



#use case of error log
try:
    value = 20/0
except ZeroDivisionError as e:
    logging.error(e)
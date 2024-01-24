# Logging Format
# https://docs.python.org/3.9/library/datetime.html
# https://docs.python.org/3.9/library/logging.html
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning('warnig message')
logging.info('info message')
logging.error('error message')

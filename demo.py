from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys

try:
    r = 3/0
    print(r)
except Exception as e:
    logging.info(e)
    raise USVisaException(e, sys)



logging.info("Logging setup complete")
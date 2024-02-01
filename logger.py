import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_file = "logs/test.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

log_format = "%(asctime)s [%(levelname)s] %(message)s"
formatter = logging.Formatter(log_format)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
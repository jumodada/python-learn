import logging

from settings.log_settings2 import set_log_config
from utils.my_db import db_utils


print_level = logging.DEBUG
set_log_config(print_level)

logging.debug("这是我主文件的debug级别的日志")
db_utils()
logging.error("我是主文件的错误级别的日志ERROR")
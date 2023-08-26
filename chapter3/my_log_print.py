# 导入日志模块
import logging

# 设置日志的输出格式
LOG_FORMAT = "%(asctime)s - %(levelname)s  - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S "
logging.basicConfig(filename='my.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    encoding="UTF-8")

logging.debug("这是调试级别的日志")
logging.info("这是详情级别的日志")
logging.warning("这是警告级别的日志")
logging.error("这是错误级别的日志")


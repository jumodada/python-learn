# 导入日志模块
import logging
def set_log_config(print_level):
    # 设置日志的输出格式
    LOG_FORMAT = "%(asctime)s - %(levelname)s  - %(message)s"
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S "
    logging.basicConfig(filename='main.log',
                        level=print_level,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT,
                        encoding="UTF-8")



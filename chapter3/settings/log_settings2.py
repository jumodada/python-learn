# 导入日志模块
import logging
def set_log_config(print_level):
    # 设置日志的输出格式
    LOG_FORMAT = "%(asctime)s - %(levelname)s  - %(message)s"
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S "

    logger = logging.getLogger()
    logger.setLevel(print_level)
    # 文件处理器，把所有的日志信息输出到文件中
    file_handler = logging.FileHandler("info.log",mode="a",encoding="UTF-8")
    logger.addHandler(file_handler)

    # 流处理器，把信息输出到控制台中
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    # 把错误日志单独输出到一个错误的文件当中
    error_handler = logging.FileHandler("error.log",mode="a",encoding="UTF-8")
    error_handler.setLevel(logging.ERROR)
    logger.addHandler(error_handler)

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
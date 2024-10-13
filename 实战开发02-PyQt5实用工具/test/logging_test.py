import logging

# 定义全局日志开关
GLOBAL_LOG_ENABLE = True

# 全局日志等级
GLOBAL_LOG_LEVEL = logging.NOTSET

# 定义不同级别的日志颜色
COLORS = {
    'DEBUG': '\033[1;32m',  # 绿色
    'INFO': '\033[1;34m',  # 蓝色
    'WARNING': '\033[38;5;208m',  # 橙色
    'ERROR': '\033[1;31m',  # 红色
    'CRITICAL': '\033[1;35m',  # 紫色
}

def get_logger(name, log_level=logging.DEBUG):
    logger = logging.getLogger(name)

    if not GLOBAL_LOG_ENABLE:
        logger.disabled = True
        return logger

    if GLOBAL_LOG_LEVEL > logging.NOTSET:
        log_level = GLOBAL_LOG_LEVEL

    logger.setLevel(log_level)
    # 定义控制台输出的handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # 定义不同级别的日志输出颜色
    for level, color in COLORS.items():
        logging.addLevelName(getattr(logging, level), f'{color}{level}{color}')

    # 定义输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    # 定义控制台输出的格式
    console_handler.setFormatter(formatter)

    # 添加handler
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.critical("-------------------------------------------log_level=Default")
    
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('signal_error message')
    logger.critical('critical message')

    logger = get_logger("test", log_level=logging.ERROR)
    logger.critical("-------------------------------------------log_level=logging.ERROR")
    
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('signal_error message')
    logger.critical('critical message')

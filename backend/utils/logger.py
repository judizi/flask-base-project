import logging
import os
from logging.handlers import TimedRotatingFileHandler


class Logger:
    __log_level_map = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    __logger = None
    __log_format = '%(asctime)s [%(levelname)s] %(message)s'

    @staticmethod
    def init(log_name="default", log_level="debug", log_dir=""):
        Logger.__logger = logging.getLogger(log_name)
        Logger.__logger.setLevel(Logger.__log_level_map.get(log_level, "debug"))
        Logger.__logger.propagate = False

        formatter = logging.Formatter(Logger.__log_format)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        Logger.__logger.addHandler(console_handler)

        if log_dir != '':
            log_dir, _ = os.path.split(log_dir)
            os.makedirs(log_dir, exist_ok=True)

            file_handler = TimedRotatingFileHandler(log_dir, when='D', interval=1, backupCount=14, encoding='utf-8')
            file_handler.setFormatter(formatter)
            Logger.__logger.addHandler(file_handler)

    @staticmethod
    def debug(message):
        Logger.__logger.debug(message)

    @staticmethod
    def info(message):
        Logger.__logger.info(message)

    @staticmethod
    def warn(message):
        Logger.__logger.warning(message)

    @staticmethod
    def error(message):
        Logger.__logger.error(message)

    @staticmethod
    def critical(message):
        Logger.__logger.critical(message)

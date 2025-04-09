import inspect
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
    __log_format = '%(asctime)s [%(levelname)s] %(custom_filename)s:%(custom_lineno)d %(message)s'

    @staticmethod
    def init(log_name, log_level, log_dir):
        if log_name == None:
            log_name = "default"

        Logger.__logger = logging.getLogger(log_name)
        Logger.__logger.setLevel(Logger.__log_level_map.get(log_level, logging.DEBUG))
        Logger.__logger.propagate = False

        formatter = logging.Formatter(Logger.__log_format)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        Logger.__logger.addHandler(console_handler)
        Logger.__get_logger_extra_data = Logger.get_logger_extra_data_with_filename

        if log_dir:
            log_dir_splitted, _ = os.path.split(log_dir)
            os.makedirs(log_dir_splitted, exist_ok=True)

            log_path = f"{log_dir}/{log_name}.log"  
            Logger.__get_logger_extra_data = Logger.get_logger_extra_data_with_fullpath
            file_handler = TimedRotatingFileHandler(log_path, when='D', interval=1, backupCount=14, encoding='utf-8')
            file_handler.setFormatter(formatter)
            Logger.__logger.addHandler(file_handler)

    @staticmethod
    def get_logger_extra_data_with_filename():
        frame = inspect.stack()[2]
        return {"custom_filename": frame.filename.split("/")[-1], "custom_lineno": frame.lineno}
    
    @staticmethod
    def get_logger_extra_data_with_fullpath():
        frame = inspect.stack()[2]
        return {"custom_filename": frame.filename, "custom_lineno": frame.lineno}

    @staticmethod
    def debug(message):
        Logger.__logger.debug(message, extra=Logger.__get_logger_extra_data())

    @staticmethod
    def info(message):
        Logger.__logger.info(message, extra=Logger.__get_logger_extra_data())

    @staticmethod
    def warn(message):
        Logger.__logger.warning(message, extra=Logger.__get_logger_extra_data())

    @staticmethod
    def error(message):
        Logger.__logger.error(message, extra=Logger.__get_logger_extra_data())

    @staticmethod
    def critical(message):
        Logger.__logger.critical(message, extra=Logger.__get_logger_extra_data())
    
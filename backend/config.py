class DevelopmentConfig():
    MODE = "Development"

    LOG_LEVEL = "debug"
    LOG_DIR = ""

    RUN_PORT ="8000"


class ProductionConfig():
    MODE = "Production"

    LOG_NAME = "rest_api"
    LOG_LEVEL = "warn"
    LOG_DIR = "/applog/web"

    RUN_PORT ="9000"


config_dict = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
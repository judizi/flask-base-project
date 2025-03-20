class DevelopmentConfig():
    MODE = "Development"

    LOG_LEVEL = "debug"
    LOG_DIR = ""

    RUN_PORT ="8000"


class ProductionConfig():
    MODE = "Production"

    LOG_LEVEL = "warn"
    LOG_DIR = "/applog/web/rest_api.log"

    RUN_PORT ="9000"


config_dict = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
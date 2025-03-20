from app import create_app
from config import config_dict
from decouple import config
from flask import current_app
from utils.logger import Logger

get_config_mode = config('ENV_NAME', default='dev', cast=str)

try:
    app_config = config_dict[get_config_mode]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [dev, prod] ')

app = create_app(app_config)
app.app_context().push()

Logger.info('Environment = ' + get_config_mode)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=current_app.config['RUN_PORT'], use_reloader=True, threaded=True)

import atexit
import os
import signal
import sys

from app.api import blueprint
from flask import Flask, current_app, redirect
from flask_cors import CORS
from utils.logger import Logger


def handle_exit():
    Logger.error(f"-> PID: {os.getpid()} killed")


def kill_handler(signum, frame):
    Logger.error(f"-> Received signal {signum}")
    sys.exit(0)


def create_app(config):
    swagger_url = "/rest/1.0"
    app = Flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(blueprint, url_prefix=swagger_url)
    CORS(app)

    with app.app_context():
        Logger.init(
            log_name=current_app.config.get('LOG_NAME', None),
            log_level=current_app.config.get('LOG_LEVEL', None),
            log_dir=current_app.config.get('LOG_DIR', None)
        )

        atexit.register(handle_exit)
        signal.signal(signal.SIGINT, kill_handler)
        signal.signal(signal.SIGTERM, kill_handler)

    @app.route('/')
    def serve():
        return redirect(swagger_url)

    return app

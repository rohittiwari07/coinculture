# # -*- coding: utf-8 -*-

# third-party imports
from flask import Flask

app = Flask(__name__)


def create_app(config_name):
    app.config.from_object('config.app_config')
    return app

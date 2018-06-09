import os
from flask import Flask
from flask_cas import CAS
from flask_cors import CORS
import click

from .api import api_bp
from .client import client_bp

from .config import current_mode


app = Flask(__name__)
app_mode = current_mode()
app.config.from_object('app.config.{}'.format(app_mode))
app.logger.info('>>> {}'.format(app_mode))

# CAS Config
app.config['CAS_SERVER'] = 'https://sso.bytedance.com/'
app.config['CAS_AFTER_LOGIN'] = '/'
CAS(app)

# Blueprints
if app_mode == 'Development': # Use this way to know Production or Development
    CORS(api_bp, supports_credentials=True) # CORS enabled for development
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

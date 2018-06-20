""" Client App """

import os
from flask import Blueprint, render_template


client_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',  # add a url path if needed, such as `/static`
                      static_folder='./dist',
                      template_folder='./dist',
                      )

from app import cas

@client_bp.route('/')
def index():
    print('username', cas.username)  # https://github.com/cameronbwhite/Flask-CAS#example
    return render_template('index.html')


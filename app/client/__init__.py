""" Client App """

import os
from flask import Blueprint, render_template
from flask_cas import login_required


client_bp = Blueprint('client_app', __name__,
                      url_prefix='',  # Add your sub-directory path if needed, such as `/my-app`
                      static_url_path='',  # Add a url path if needed, such as `/static`
                      static_folder='./dist',
                      template_folder='./dist',
                      )

from app import cas
from app.config import current_mode


if current_mode() == 'Development':
    # Do not use CAS in development mode
    login_required = lambda x: x


@client_bp.route('/')
@login_required
def index():
    print('username', cas.username)  # https://github.com/cameronbwhite/Flask-CAS#example
    return render_template('index.html')


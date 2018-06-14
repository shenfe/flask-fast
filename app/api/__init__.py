""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session


api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   url_prefix='/api')


@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


from .normal import normal_route
normal_route(api_bp)

from flask_restplus import Api
api = Api(api_bp, doc='/doc/')

from .rest import rest_route
rest_route(api)


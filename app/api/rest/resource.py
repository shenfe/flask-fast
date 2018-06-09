"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

import json
from datetime import datetime
from flask import request
from flask_restplus import fields
from .base import BaseResource, SecureResource

from ...util.fieldify import fields_of, data_of


def rest_route(api):


    mock_mods = {}
    def mock_mod(name):
        if mock_mods.has_key(name):
            return mock_mods.get(name)
        mock_mods[name] = api.model(name, fields_of(name + '.json'))
        return mock_mods[name]
    def mock_data(name):
        return data_of(name + '.json')


    # Generate a parser for in-query params
    def query_parser(example):
        parser = api.parser()
        for name, value in example.iteritems():
            parser.add_argument(name, type=type(value), default=value, location='path')
        return parser


    # Generate a parser for form params
    def form_parser(example):
        parser = api.parser()
        for name, value in example.iteritems():
            parser.add_argument(name, type=type(value), default=value, location='form')
        return parser

    # (Example) Define a model
    sample_model = api.model('SampleResource', {
        'name': fields.String(description='The resource name', required=True, example='Jack')
    })

    # (Example) Define a parser for input params
    sample_parser = api.parser()
    sample_parser.add_argument('param', type=int, help='Some param', location='path')

    @api.route('/resource/<string:resource_id>')
    @api.doc(params={'resource_id': 'ID of resource example 1'}) # (For Swagger) Include additional information in the documentation, for both class or method
    class ResourceOne(BaseResource):

        @api.expect(query_parser({'id': 1})) # (For Swagger)
        @api.response(200, 'Success', mock_mod('res1')) # (For Swagger) Document the known responses; shortcut for `@api.doc(responses=...`
        @api.response(400, 'Validation Error') # (For Swagger)
        def get(self, resource_id):
            return mock_data('res1')

        @api.expect(form_parser({'name': 'Tom'})) # (For Swagger) Specify the expected input fields
        def put(self, resource_id):
            form_data = request.form
            return {'code': 0, 'data': form_data}

        @api.expect(sample_model) # (For Swagger) Specify the expected input fields
        def post(self, resource_id):
            json_payload = request.json
            return {'code': 0, 'data': json_payload}, 201


    @api.route('/secure-resource/<string:resource_id>')
    @api.param('resource_id', 'ID of resource example 2') # (For Swagger) Shortcut for `@api.doc(params={...`
    class ResourceTwo(SecureResource):

        def get(self, resource_id):
            timestamp = datetime.utcnow().isoformat()
            return {'timestamp': timestamp}

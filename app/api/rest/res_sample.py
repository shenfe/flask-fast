"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

import json
from datetime import datetime
from flask import request
from flask_restplus import fields
from werkzeug.datastructures import FileStorage

from .base import BaseResource, SecureResource
from .helper import mock_mod, mock_data, query_parser, form_parser, Mod


def mount(api):

    # (Example) Define a model
    sample_model = Mod('SampleResource', {
        'name': fields.String(description='The resource name', required=True, example='Jack')
    })

    # (Example) Define a parser
    sample_parser = api.parser()
    sample_parser.add_argument('avatar', type=FileStorage, location='files', help='user avatar')
    sample_parser.add_argument('name', type=str, location='form', help='user name')
    sample_parser.add_argument('age', type=int, location='form', help='user age')

    @api.route('/resource/<string:resource_id>')
    # (For Swagger) Include additional information in the documentation, for both class or method
    @api.doc(params={'resource_id': 'ID of resource 1'})
    class ResourceOne(BaseResource):

        @api.expect(query_parser({'id': 1}))  # (For Swagger)
        # (For Swagger) Document the known responses; shortcut for `@api.doc(responses=...`
        @api.response(200, 'Success', mock_mod('res1'))
        @api.response(400, 'Validation Error')  # (For Swagger)
        def get(self, resource_id):
            """Fetch a resource"""
            return mock_data('res1')

        # (For Swagger) Specify the expected input fields
        @api.expect(form_parser({'name': 'Tom'}))
        def put(self, resource_id):
            form_data = request.form
            return {'code': 0, 'data': form_data}

        # (For Swagger) Specify the expected input fields
        @api.expect(sample_model)
        def post(self, resource_id):
            """Update a resource"""
            json_payload = request.json
            return {'code': 0, 'data': json_payload}, 201

    @api.route('/secure-resource/<string:resource_id>')
    # (For Swagger) Shortcut for `@api.doc(params={...`
    @api.param('resource_id', 'ID of resource 2')
    class ResourceTwo(SecureResource):

        def get(self, resource_id):
            timestamp = datetime.utcnow().isoformat()
            return {'timestamp': timestamp}

from flask import request, make_response, jsonify, send_file
from flask_cas import login_required
import json

from app.config import current_mode


def normal_route(app):

    @app.route('/sum', methods=['GET', 'POST'])
    def calc_sum():
        return json.dumps(2)

    @app.route('/res/<int:id>', methods=['GET', 'POST'])
    def res(id):
        return json.dumps({'code': 0, 'res': id})

    @app.route('/user-profile', methods=['GET', 'POST'])
    @login_required
    def get_user_profile():
        return json.dumps({'name': 'Tom'})

    @app.route('/test-post', methods=['POST'])
    def post_echo():
        print json.dumps(request.json)
        response = make_response(jsonify(code=0, message='success'))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST,OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
        return response


    if current_mode() == 'Development':

        # Expose `swagger.json` file
        @app.route('/all', methods=['GET'])
        def display_swagger():
            return send_file('api/swagger.json')

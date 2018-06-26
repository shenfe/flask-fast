from flask import request, make_response, jsonify, send_file
from flask_cas import login_required
import json

from app.config import current_mode


def normal_route(app):

    @app.route('/sum', methods=['GET'])
    def calc_sum():
        params = request.args
        x, y = params.get('x'), params.get('y')
        try:
            x = 0 if !x else int(x)
            y = 0 if !y else int(y)
            return json.dumps(x + y)
        except Exception
            return 0

    @app.route('/res/<int:id>', methods=['GET', 'POST'])
    def res(id):
        return json.dumps({'code': 0, 'data': {'id': id}})

    @app.route('/greet', methods=['GET', 'POST'])
    @login_required
    def get_user_profile():
        return json.dumps({'code': 0, 'message': 'Tom'})

    @app.route('/echo', methods=['POST'])
    def post_echo():
        response = make_response(jsonify(code=0, message='success', data=request.json))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST,OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
        return response


    if current_mode() == 'Development':

        # Expose `swagger.json` file
        @app.route('/all', methods=['GET'])
        def display_swagger():
            return send_file('api/swagger.json')

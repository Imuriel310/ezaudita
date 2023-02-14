from chalice import Chalice
import services.unit_measure_service as unit_measure
from services.utils import validate_request
from chalice import Response
from chalice import BadRequestError
import models.request_schema as request_model
import json
# import requests

app = Chalice(app_name='ezaudita')
# from database import config


@app.route(
    '/unit_measure',
    methods=['GET', 'POST', 'PUT', 'DELETE']
)
def get_unit_measure():
    method = app.current_request.method
    if method == 'GET':
        params = app.current_request.query_params
        response, status_code = unit_measure.get_unit_measure(params)
    if method == 'POST':
        body = app.current_request.json_body
        validate_request(body, request_model.unit_measure_model)
        response, status_code = unit_measure.create_unit_measure(body)
    if method == 'PUT':
        params = app.current_request.query_params
        unit_measure_id = params.get('unit_measure_id')
        # verify param
        if unit_measure_id is None:
            raise BadRequestError(
                'param unit_measure_id requiered'
            )
        #verify body
        body = app.current_request.json_body
        validate_request(body, request_model.unit_measure_model)
        response, status_code = unit_measure.update_unit_measure_name(body, unit_measure_id)
        
    return Response(
        body = response,
        status_code=status_code,
        headers={'Content-Type': 'application/json'}
    )
#

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

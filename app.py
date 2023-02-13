from chalice import Chalice
import services.unit_measure_service as unit_measure
from chalice import Response
# import requests

app = Chalice(app_name='ezaudita')
# from database import config


@app.route(
    '/unit_measure',
    methods=['GET']
)
def get_unit_measure():
    method = app.current_request.method
    if method == 'GET':
        params = app.current_request.query_params
        response = unit_measure.get_unit_measure(params)
    if method == 'POST':
        body = None
        response = unit_measure.create_unit_measure(body)
    return Response(
        body = response,
        status_code=200,
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

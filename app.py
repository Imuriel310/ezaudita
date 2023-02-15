from chalice import Chalice
import services.unit_measure_service as unit_measure
import services.products_service as proudct
import services.sales as sale
from services.utils import validate_request
from chalice import Response
from chalice import BadRequestError
from chalice import NotFoundError
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
    
@app.route(
    '/product',
    methods=['GET', 'POST', 'PUT', 'DELETE']
)
def product():
    method = app.current_request.method
    if method == 'GET':
        params = app.current_request.query_params or {}
        response, status_code = proudct.get_products(params)
    if method == 'POST':
        body = app.current_request.json_body
        validate_request(body, request_model.create_product_model)
        response, status_code = proudct.create_product(body)
    if method == 'PUT':
        params = app.current_request.query_params or {}
        product_id = params.get('product_id')
        # verify param
        if product_id is None:
            raise BadRequestError(
                'param product_id requiered'
            )
        #verify body
        body = app.current_request.json_body
        validate_request(body, request_model.update_product_model)
        response, status_code = proudct.update_product(body, product_id)
    
    if status_code == 404:
        raise NotFoundError("No products found")
    return Response(
        body = response,
        status_code=status_code,
        headers={'Content-Type': 'application/json'}
    )
    
@app.route(
    '/sales',
    methods=['GET', 'POST']
)
def sales():
    method = app.current_request.method
    if method == 'GET':
        params = app.current_request.query_params or {}
        response, status_code = sale.get_sales(params)
    if method == 'POST':
        body = app.current_request.json_body
        validate_request(body, request_model.create_sales_model)
        response, status_code = sale.create_sales(body)
    if status_code == 404:
        raise NotFoundError("no registrers found")
    return Response(
        body = response,
        status_code=status_code,
        headers={'Content-Type': 'application/json'}
    )

@app.route('/sales_each', methods=['GET'])
def sales_each_product():
    response = sale.get_sales_each_product()
    return Response(
        body = response,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )

@app.route('/sales_all', methods=['GET'])
def sales_all_products():
    response = sale.get_sales_all_products()
    return Response(
        body = response,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )
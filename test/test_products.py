from chalice.test import Client
from app import app
import pytest
import json
class TestProducts():
    
    def test_save_products(self):
        # TESTS TO OK
        with Client(app) as client:
            request = {
                "name": "new_product",
                "price": 20,
                "unit_measure_id": 10
            }
            result = client.http.post('/product', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.product_id = result.json_body.get('product_id')
            assert result.status_code == 201

    def test_get_all_products(self):
        with Client(app) as client:
            result = client.http.get('/product')
            assert result.status_code == 200

    def test_get_products(self):
        with Client(app) as client:

            result = client.http.get('/product?product_id='+str(pytest.product_id))
            assert result.status_code == 200
    
    def test_edit_products(self):
        with Client(app) as client:
            request = {
                "name": "new name product"
            }
            result = client.http.put(
                f'/product?product_id={pytest.product_id}',
                body=json.dumps(request),
                headers={'Content-Type':'application/json'}
            )
            assert result.status_code == 200
    def test_delete_products(self):
        with Client(app) as client:
            result = client.http.delete(f'/product?product_id={pytest.product_id}')
            assert result.status_code == 200
            
    # TEST TO FAIL
    def test_get_products_non_existent(self):
        with Client(app) as client:

            result = client.http.get('/product?product_id=0')
            assert result.status_code == 404
    def test_delete_products_non_existent(self):
        with Client(app) as client:

            result = client.http.delete('/product?product_id=0')
            assert result.status_code == 404
    
    def test_save_incorrect_products(self):
        # TESTS TO OK
        with Client(app) as client:
            request = {
                "incorrect_payload": "new unit test"
            }
            result = client.http.post('/product', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.product_id = result.json_body.get('products_id')
            assert result.status_code == 400
    def test_save_incorrect_products_with_incorrect_unit_measure(self):
        # TESTS TO OK
        with Client(app) as client:
            request = {
                "name": "new_product",
                "price": 20,
                "unit_measure_id": 1000000
            }
            result = client.http.post('/product', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.product_id = result.json_body.get('products_id')
            assert result.status_code == 500

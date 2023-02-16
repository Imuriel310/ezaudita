from chalice.test import Client
from app import app
import pytest
import json
TEST_UNIT_MEASURE_ID = 0
unit_measure_id = None
class TestSales():
    
    def test_save_sale(self):
        # TESTS TO OK
        with Client(app) as client:
            request = {
                "quantity": 15,
                "date": "15/02/2023",
                "product_id": 2
            }
            result = client.http.post('/sales', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.sales_id = result.json_body.get('sales_id')
            assert result.status_code == 201
            
    def test_get_all_sales(self):
        with Client(app) as client:
            result = client.http.get('/sales')
            assert result.status_code == 200
    def test_delete_sale(self):
        with Client(app) as client:
            print(pytest.sales_id)
            result = client.http.delete(f'/sales?sales_id={pytest.sales_id}')
            assert result.status_code == 200
    def test_get_all_sales(self):
        with Client(app) as client:
            result = client.http.get('/sales_all')
            assert result.status_code == 200
    def test_get_sales_each(self):
        with Client(app) as client:
            result = client.http.get('/sales_each')
            assert result.status_code == 200
            
            
    # #TEST TO FAIL
    def test_save_incorrect_sales(self):
        with Client(app) as client:
            request = {
                "incorrect_payload": "asd"
            }
            result = client.http.post('/sales', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.unit_measure_id = result.json_body.get('unit_measure_id')
            assert result.status_code == 400
    def test_save_incorrect_sales(self):
        with Client(app) as client:
            request = {
        "quantity": 15,
        "date": "15/02/2023",
        "product_id": 1000
}
            result = client.http.post('/sales', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.unit_measure_id = result.json_body.get('unit_measure_id')
            assert result.status_code == 500
            
    
    # def test_get_unit_measure_non_existent(self):
    #     with Client(app) as client:

    #         result = client.http.get('/unit_measure?unit_measure_id=0')
    #         assert result.status_code == 404
    # def test_delete_unit_measure_non_existent(self):
    #     with Client(app) as client:

    #         result = client.http.delete('/unit_measure?unit_measure_id=0')
    #         assert result.status_code == 404
    

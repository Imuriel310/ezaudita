from chalice.test import Client
from app import app
import pytest
import json

class TestUnitMeasure():
    
    def test_save_unit_measure(self):
        # TESTS TO OK
        with Client(app) as client:
            request = {
                "name": "new unit test"
            }
            result = client.http.post('/unit_measure', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.unit_measure_id = result.json_body.get('unit_measure_id')
            assert result.status_code == 201
            
    def test_get_all_unit_measure(self):
        with Client(app) as client:
            result = client.http.get('/unit_measure')
            assert result.status_code == 200

    def test_get_unit_measure(self):
        with Client(app) as client:
            print(pytest.unit_measure_id)

            result = client.http.get('/unit_measure?unit_measure_id='+str(pytest.unit_measure_id))
            assert result.status_code == 200
    def test_edit_unit_measure(self):
        with Client(app) as client:
            request = {
                "name": "new name test"
            }
            result = client.http.put(
                f'/unit_measure?unit_measure_id={pytest.unit_measure_id}',
                body=json.dumps(request),
                headers={'Content-Type':'application/json'}
            )
            assert result.status_code == 200
    def test_delete_unit_measure(self):
        with Client(app) as client:
            result = client.http.delete(f'/unit_measure?unit_measure_id={pytest.unit_measure_id}')
            assert result.status_code == 200
            
    #TEST TO FAIL
    def test_get_unit_measure_non_existent(self):
        with Client(app) as client:

            result = client.http.get('/unit_measure?unit_measure_id=0')
            assert result.status_code == 404
    def test_delete_unit_measure_non_existent(self):
        with Client(app) as client:

            result = client.http.delete('/unit_measure?unit_measure_id=0')
            assert result.status_code == 404
    def test_save_incorrect_unit_measure(self):
        # TESTS TO OK
        with Client(app) as client:
            request = {
                "incorrect_payload": "new unit test"
            }
            result = client.http.post('/unit_measure', body=json.dumps(request),  headers={'Content-Type':'application/json'})
            print(result.json_body)
            pytest.unit_measure_id = result.json_body.get('unit_measure_id')
            assert result.status_code == 400

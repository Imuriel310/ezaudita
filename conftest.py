import pytest

def pytest_configure():
    pytest.unit_measure_id = None
    pytest.product_id = None
    pytest.sales_id = None
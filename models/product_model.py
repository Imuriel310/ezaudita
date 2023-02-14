from datetime import date

class ProductModel:

    def __init__(self,
                product_id = None,
                name = None,
                price = None,
                unit_measure_id = None):
        """Constructor"""
        self.product_id = product_id
        self.name = name
        self.price = price
        self.unit_measure_id = unit_measure_id
        

    product_id: int
    name: str
    price: float
    unit_measure_id: int
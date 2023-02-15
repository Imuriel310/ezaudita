from datetime import date

class SalesModel:

    def __init__(self,
                sales_id = None,
                date = None,
                quantity = None,
                product_id = None):
        """Constructor"""
        self.sales_id = sales_id
        self.date = date
        self.quantity = quantity
        self.product_id = product_id
        

    sales_id: int
    date: str
    quantity: float
    unit_measure_id: int

class SalesEach:

    def __init__(self,
                product_id = None,
                product_name = None,
                unit_measure = None,
                quantity = None,
                amount = None):
        """Constructor"""
        self.product_id = product_id
        self.product_name = product_name
        self.unit_measure = unit_measure
        self.quantity = quantity
        self.amount = amount
        
    product_id: int
    product_name: int
    unit_measure: str
    quantity: int
    amount: float
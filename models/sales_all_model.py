
class SalesAll:

    def __init__(self,
                quantity = None,
                amount = None):
        """Constructor"""
        self.total_quantity = quantity
        self.total_amount = amount
        
    total_quantity: int
    total_amount: float
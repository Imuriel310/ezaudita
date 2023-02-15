import dao.sales_dao as dao
from models.sales_model import SalesModel
from models.sales_each_model import SalesEach
from models.sales_all_model import SalesAll


def get_sales(params: dict) -> list:

    response_list = []
    filter_dict = {}
    if params.get('sales_id'): filter_dict.update({'sales_id': params['sales_id']}) 
    if params.get('date'): filter_dict.update({'date': params['date']}) 
    if params.get('quantity'): filter_dict.update({'quantity': params['quantity']}) 
    if params.get('product_id'): filter_dict.update({'product_id': params['product_id']}) 
    
    if filter_dict:
        response = dao.get_sales_specific(filter_dict)
    else:
        response =  dao.get_sales_all()
    for row in response:
        response_list.append(
            SalesModel(
                sales_id=row.sales_id,
                date=str(row.date),
                quantity=row.quantity,
                product_id=row.product_id
            ).__dict__
        )
    return response_list,  200 if response_list else 404

def create_sales(body:dict) -> dict:
    sales_model = SalesModel(
        date = body.get('date'),
        quantity = body.get('quantity'),
        product_id = body.get('product_id')
    )
    return dao.create_sales(sales_model), 201
def get_sales_each_product():
    response = []
    products_sales = dao.get_sales_each_product()
    for sale in products_sales:
        response.append(SalesEach(
                sale.product,
                sale.unit_measure,
                sale.quantity,
                sale.amount
            ).__dict__
        )
    
    return response

def get_sales_all_products():
    products_sales = dao.get_sales_all_products()[0]
    return SalesAll(
            products_sales.total_quantity,
            float(products_sales[1])
        ).__dict__
# def update_product(body:dict, product_id: int) -> dict:
#     product_model = SalesModel(
#         name=body.get('name'),
#         price=body.get('price'),
#         unit_measure_id=body.get('unit_measure_id')
#     )
#     return dao.update_product(product_id, product_model)
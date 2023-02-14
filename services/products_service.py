import dao.products_dao as dao
from models.product_model import ProductModel


def get_products(params: dict) -> list:

    response_list = []
    filter_dict = {}
    if params.get('product_id'): filter_dict.update({'product_id': params['product_id']}) 
    if params.get('name'): filter_dict.update({'name': params['name']}) 
    if params.get('price'): filter_dict.update({'price': params['price']}) 
    if params.get('unit_measure_id'): filter_dict.update({'unit_measure_id': params['unit_measure_id']}) 
    
    if filter_dict:
        response = dao.get_product_specific(filter_dict)
    else:
        response =  dao.get_products_all()
    for row in response:
        response_list.append(
            ProductModel(
                product_id=row.product_id,
                name = row.name,
                price = row.price,
                unit_measure_id=row.unit_measure_id
            ).__dict__
        )
    return response_list,  200 if response_list else 404

def create_product(body:dict) -> dict:
    product_model = ProductModel(
        name=body.get('name'),
        price=body.get('price'),
        unit_measure_id=body.get('unit_measure_id')
    )
    return dao.create_product(product_model), 201

def update_product(body:dict, product_id: int) -> dict:
    product_model = ProductModel(
        name=body.get('name'),
        price=body.get('price'),
        unit_measure_id=body.get('unit_measure_id')
    )
    return dao.update_product(product_id, product_model)
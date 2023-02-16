import dao.products_dao as dao  # imports the data access object for products
from models.product_model import ProductModel  # imports the model for products

def get_products(params: dict) -> list:
    response_list = [] 
    filter_dict = {}  
    
    # Adds the filter parameters to the filter dictionary if they exist in the query parameters
    if params.get('product_id'): filter_dict.update({'product_id': params['product_id']}) 
    if params.get('name'): filter_dict.update({'name': params['name']}) 
    if params.get('price'): filter_dict.update({'price': params['price']}) 
    if params.get('unit_measure_id'): filter_dict.update({'unit_measure_id': params['unit_measure_id']}) 
    
    # Calls the appropriate DAO method to retrieve the products based on the filter dictionary
    if filter_dict:
        response = dao.get_product_specific(filter_dict)
    else:
        response =  dao.get_products_all()
    
    # Transforms the response rows into ProductModel objects and adds them to the response list
    for row in response:
        response_list.append(
            ProductModel(
                product_id=row.product_id,
                name = row.name,
                price = row.price,
                unit_measure_id=row.unit_measure_id
            ).__dict__
        )
    # Returns the response list with an appropriate status code based on whether any products were found
    return response_list,  200 if response_list else 404

# This function creates a new product in the database based on the given request body
def create_product(body:dict) -> dict:
    product_model = ProductModel(
        name=body.get('name'),
        price=body.get('price'),
        unit_measure_id=body.get('unit_measure_id')
    )
    # Calls the DAO method to create the new product and returns the result with a 201 status code
    return dao.create_product(product_model), 201

# This function updates an existing product in the database based on the given request body and product ID
def update_product(body:dict, product_id: int) -> dict:
    product_model = ProductModel(
        name=body.get('name'),
        price=body.get('price'),
        unit_measure_id=body.get('unit_measure_id')
    )
    # Calls the DAO method to update the product and returns the result
    return dao.update_product(product_id, product_model)

# This function deletes an existing product from the database based on the given product ID
def delete_product(product_id:int) -> dict:
    # Calls the DAO method to delete the product and returns a success message with a 200 status code
    dao.delete_product(product_id)
    return {'message':'product deleted'}, 200
import dao.sales_dao as dao
from models.sales_model import SalesModel
from models.sales_each_model import SalesEach
from models.sales_all_model import SalesAll

# Function to get sales records based on filter parameters
def get_sales(params: dict) -> list:
    response_list = []
    filter_dict = {}
    if params.get('sales_id'): filter_dict.update({'sales_id': params['sales_id']}) 
    if params.get('date'): filter_dict.update({'date': params['date']}) 
    if params.get('quantity'): filter_dict.update({'quantity': params['quantity']}) 
    if params.get('product_id'): filter_dict.update({'product_id': params['product_id']}) 
    
    # Check if any filters were applied, get specific sales records
    if filter_dict:
        response = dao.get_sales_specific(filter_dict)
    # Otherwise, get all sales records
    else:
        response =  dao.get_sales_all()
    # Convert sales records into SalesModel objects and append to response list
    for row in response:
        response_list.append(
            SalesModel(
                sales_id=row.sales_id,
                date=str(row.date),
                quantity=row.quantity,
                product_id=row.product_id
            ).__dict__
        )
    # Return response list and status code 200 if list is not empty, otherwise return status code 404
    return response_list,  200 if response_list else 404

# Function to create a new sales record
def create_sales(body:dict) -> dict:
    # Create a SalesModel object using values from request body
    sales_model = SalesModel(
        date = body.get('date'),
        quantity = body.get('quantity'),
        product_id = body.get('product_id')
    )
    # Call DAO function to add new sales record to the database, and return with status code 201
    return dao.create_sales(sales_model), 201

# Function to get sales records for each product
def get_sales_each_product():
    response = []
    # Get sales records for each product from the database using DAO function
    products_sales = dao.get_sales_each_product()
    # Convert each sales record into a SalesEach object and append to response list
    for sale in products_sales:
        response.append(SalesEach(
                sale.product_id,
                sale.product,
                sale.unit_measure,
                sale.quantity,
                sale.amount
            ).__dict__
        )
    # Return response list
    return response

# Function to get sales totals for all products
def get_sales_all_products():
    # Get total sales quantity and revenue for all products from the database using DAO function
    products_sales = dao.get_sales_all_products()[0]
    # Convert sales totals into a SalesAll object and return
    return SalesAll(
            products_sales.total_quantity,
            float(products_sales[1])
        ).__dict__

# Function to delete a sales record
def delete_sale(sale_id:int) -> dict:
    # Call DAO function to delete sales record with given ID from the database
    dao.delete_sale(sale_id)
    # Return success message with status code 200
    return {'message':'sale deleted'}, 200
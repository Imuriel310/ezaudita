# import necessary modules and classes
from sqlalchemy.orm.session import Session
from sqlalchemy import func
from entity.sales import Sales
from entity.products import Products
from entity.unit_measure import UnitMeasure
from models.sales_model import SalesModel
import sqlalchemy

# import database configuration and Chalice errors
from database.config import SessionLocal
from chalice import ChaliceViewError
from chalice import NotFoundError


# function to get all sales
def get_sales_all() -> dict:
    with SessionLocal() as session:
        # retrieve all rows from the Sales table
        sales_data = session.query(Sales).all()
        return sales_data


# function to get specific sales based on given parameters
def get_sales_specific(dict:dict) -> object:
    with SessionLocal() as session:
        # retrieve rows from the Sales table that match the given parameters
        sales_data = session.query(Sales).filter_by(
            **dict
        ).all()
        return sales_data


# function to create a new sale
def create_sales(sales_object: SalesModel) -> dict:
    with SessionLocal() as session:
        # create a new Sale object and set its attributes based on the input data
        new_sale = Sales()
        new_sale.date = sales_object.date
        new_sale.quantity = sales_object.quantity
        new_sale.product_id = sales_object.product_id
        try:
            # add the new Sale object to the session and commit the transaction
            session.add(new_sale)
            session.flush()
            session.commit()
        except Exception as e:
            # if an error occurs, raise a ChaliceViewError with the error message
            raise ChaliceViewError(
                e
            )
        # return a success message and the ID of the newly created Sale object
        return  {'message': 'sale created', 'sales_id':new_sale.sales_id }


# function to delete a sale based on its ID
def delete_sale(sale_id:int):
    with SessionLocal() as session:
        try:
            # delete the Sale object with the given ID from the Sales table
            deleted = session.query(Sales).filter(
                Sales.sales_id==sale_id
            ).delete()
        
            session.flush()
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            # if an integrity error occurs, raise a ChaliceViewError with a custom error message
            raise ChaliceViewError(
                f"Integrity error, probably unit measure id is being referenced in other table"
            )
        except Exception as e:
            # if any other error occurs, raise a ChaliceViewError with the error message
            raise ChaliceViewError(
                e
            )
        # if no rows were deleted, raise a NotFoundError with a custom error message
        if deleted == 0:
                raise NotFoundError(
                    'sale not found'
        
        )
        
# this function returns a dictionary with the total quantity of all products sold 
# and the total amount of sales for all products
def get_sales_all_products() -> dict:
    with SessionLocal() as session:
        # create a subquery to calculate the total amount of sales per product
        subq_price_per_product = session.query(
            (func.sum(Sales.quantity)*Products.price).label('suma')
        ).join(
            Sales, Sales.product_id == Products.product_id,
        ).group_by(Products.product_id).subquery()
        
        # calculate the sum of total sales by adding up the total amount of sales per product
        subq_sum_total_price = session.query(
            func.sum(subq_price_per_product.c.suma).label('suma_total')
        ).scalar()
        
        # query to get the total quantity of all products sold and the total amount of sales
        response = session.query(
            (func.sum(Sales.quantity)).label('total_quantity'),
            subq_sum_total_price
        ).all()
        return response

# this function returns a list with the name of each product, its unit of measure, the 
# total quantity sold, and the total amount of sales for each product
def get_sales_each_product() -> list:
    with SessionLocal() as session:
        response = session.query(
            Products.name.label('product'), 
            # if None then 0
            UnitMeasure.name.label('unit_measure'),
            func.coalesce(
                func.sum(Sales.quantity), 0
            ).label('quantity'),

            func.coalesce(
                func.sum(Sales.quantity)*Products.price, 0
            ).label('amount')

        ).join(
            Sales, Sales.product_id == Products.product_id,
            isouter = True
        ).join(
            UnitMeasure, UnitMeasure.unit_measure_id == Products.unit_measure_id
        ).group_by(Products.product_id, UnitMeasure.name).all()

        return response
        
        
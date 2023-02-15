from sqlalchemy.orm.session import Session
from sqlalchemy import func
from entity.sales import Sales
from entity.products import Products
from entity.unit_measure import UnitMeasure
from models.sales_model import SalesModel

from database.config import SessionLocal
from chalice import ChaliceViewError
from chalice import NotFoundError

def get_sales_all() -> dict:
    with SessionLocal() as session:
        sales_data = session.query(Sales).all()
        return sales_data

def get_sales_specific(dict:dict) -> object:
    with SessionLocal() as session:
        sales_data = session.query(Sales).filter_by(
            **dict
        ).all()
        return sales_data

def create_sales(sales_object: SalesModel) -> dict:
    with SessionLocal() as session:
        new_sale = Sales()
        new_sale.date = sales_object.date
        new_sale.quantity = sales_object.quantity
        new_sale.product_id = sales_object.product_id
        try:
            session.add(new_sale)
            session.commit()
        except Exception as e:
            raise ChaliceViewError(
                e
            )
        return 200
def get_sales_all_products() -> dict:
    with SessionLocal() as session:
        subq_price_per_product = session.query(
            (func.sum(Sales.quantity)*Products.price).label('suma')
        ).join(
            Sales, Sales.product_id == Products.product_id,
        ).group_by(Products.product_id).subquery()
        
        subq_sum_total_price = session.query(
            func.sum(subq_price_per_product.c.suma).label('suma_total')
        ).scalar()
        
        response = session.query(
            (func.sum(Sales.quantity)).label('total_quantity'),
            subq_sum_total_price
        ).all()
        return response
def get_sales_each_product() -> list:
    with SessionLocal() as session:
        # CUATRO
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

        
        
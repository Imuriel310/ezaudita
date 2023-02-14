from entity.products import Products
from database.config import SessionLocal
from chalice import ChaliceViewError
from chalice import NotFoundError
from models.product_model import ProductModel
import sqlalchemy

def get_products_all() -> object:
    with SessionLocal() as session:
        unit_measure_data = session.query(Products).all()
        return unit_measure_data

def get_product_specific(dict:dict) -> object:
    with SessionLocal() as session:
        products_data = session.query(Products).filter_by(
            **dict
        ).all()
        return products_data
        
def create_product(product: ProductModel) -> dict:
    with SessionLocal() as session:
        new_product = Products()
        new_product.name = product.name
        new_product.price = product.price
        new_product.unit_measure_id = product.unit_measure_id
        # new_unit_measure.name = 
        try:
            session.add(new_product)
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            raise ChaliceViewError(
                f"Integrity error unit measure id {product.unit_measure_id} does not exist"
            )
        except Exception as e:
            raise ChaliceViewError(
                e
            )
        return {'message': 'product created'}

def update_product(product_id: int, product_object: ProductModel) -> dict and int:
    with SessionLocal() as session:
        product_row = session.query(Products).filter(
            Products.product_id==product_id
        ).first()
        if product_row is None:
            raise NotFoundError("product not found")
        try:
            if product_object.name:
                product_row.name = product_object.name
            if product_object.price:
                product_row.price = product_object.price
            if product_object.unit_measure_id:
                product_row.unit_measure_id = product_object.unit_measure_id
            session.flush()
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            raise ChaliceViewError(
                f"Integrity error unit measure id {product_object.unit_measure_id} does not exist"
            )
        except Exception as e:
            raise ChaliceViewError(
                e
            )
        return {'message': 'product updated'}, 200
        
        
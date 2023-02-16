from entity.products import Products
from database.config import SessionLocal
from chalice import ChaliceViewError
from chalice import NotFoundError
from models.product_model import ProductModel
import sqlalchemy

# Get all products from the database
def get_products_all() -> object:
    with SessionLocal() as session:
        unit_measure_data = session.query(Products).all()
        return unit_measure_data

# Get a specific product from the database based on a dictionary of filters
def get_product_specific(dict:dict) -> object:
    with SessionLocal() as session:
        products_data = session.query(Products).filter_by(
            **dict
        ).all()
        return products_data

# Create a new product in the database
def create_product(product: ProductModel) -> dict:
    with SessionLocal() as session:
        new_product = Products()
        new_product.name = product.name
        new_product.price = product.price
        new_product.unit_measure_id = product.unit_measure_id

        # Try to add the new product to the database, and catch any errors that might occur
        try:
            session.add(new_product)
            session.flush()
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            raise ChaliceViewError(
                f"Integrity error unit measure id {product.unit_measure_id} does not exist"
            )
        except Exception as e:
            raise ChaliceViewError(
                e
            )

        # Return a dictionary indicating that the product was created, along with its new product_id
        return {'message': 'product created', 'product_id': new_product.product_id}

# Update an existing product in the database based on a product_id and a ProductModel object
def update_product(product_id: int, product_object: ProductModel) -> dict and int:
    with SessionLocal() as session:
        product_row = session.query(Products).filter(
            Products.product_id==product_id
        ).first()

        # If the product_id is not found in the database, raise a NotFoundError
        if product_row is None:
            raise NotFoundError("product not found")

        # Update the fields of the product based on the fields of the ProductModel object, and catch any errors
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

        # Return a dictionary indicating that the product was updated
        return {'message': 'product updated'}, 200

# Delete an existing product from the database based on a product_id
def delete_product(product_id:int):
    with SessionLocal() as session:
        try:
            deleted = session.query(Products).filter(
                Products.product_id==product_id
            ).delete()
        
            session.flush()
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            raise ChaliceViewError(
                f"Integrity error, probably product id is being referenced in other table"
            )
        except Exception as e:
            raise ChaliceViewError(
                e
            )

        # If no rows were deleted from the database, raise a NotFoundError
        if deleted == 0:
            raise NotFoundError('product not found')
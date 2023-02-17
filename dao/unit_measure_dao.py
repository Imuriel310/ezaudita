from sqlalchemy.orm.session import Session
from entity.unit_measure import UnitMeasure
from database.config import SessionLocal
from chalice import ChaliceViewError
from chalice import NotFoundError
import sqlalchemy

def get_unit_measure_all() -> dict:
    with SessionLocal() as session:
        # Retrieve all unit measures from the database
        unit_measure_data = session.query(UnitMeasure).all()
        return unit_measure_data

def get_unit_measure_specific(unit_measure_id:int = None) -> dict:
    with SessionLocal() as session:
        # Retrieve a specific unit measure from the database
        unit_measure_data = session.query(UnitMeasure).filter(
            UnitMeasure.unit_measure_id==unit_measure_id
        ).first()
        return unit_measure_data
        
def save_unit_measure(name: str) -> dict:
    with SessionLocal() as session:
        # Create a new unit measure in the database with the given name
        new_unit_measure = UnitMeasure()
        new_unit_measure.name = name
        try:
            session.add(new_unit_measure)
            session.flush()
            session.commit()
        except Exception as e:
            # If an error occurs, raise a ChaliceViewError with the error message
            raise ChaliceViewError(
                e
            )
        return {'message': 'unit measure created', 'unit_measure_id':new_unit_measure.unit_measure_id }

def update_unit_measure(unit_measure_new_name: str, unit_measure_id: int) -> dict:
    with SessionLocal() as session:
        # Update the name of a unit measure in the database
        unit_measure_row = session.query(UnitMeasure).filter(
            UnitMeasure.unit_measure_id==unit_measure_id
        ).first()
        if unit_measure_row is None:
            # If the unit measure is not found, raise a NotFoundError
            raise NotFoundError("unit measure not found")
        try:
            unit_measure_row.name = unit_measure_new_name
            session.flush()
            session.commit()
        except Exception as e:
            # If an error occurs, raise a ChaliceViewError with the error message
            raise ChaliceViewError(
                e
            )
        return {'message': 'unit measured updated'}

def delete_unit_measure(unit_measure_id:int):
    # Create a session to interact with the database.
    with SessionLocal() as session:
        try:
            # Use the session to query the `UnitMeasure` table and delete the row with the given `unit_measure_id`.
            deleted = session.query(UnitMeasure).filter(
                UnitMeasure.unit_measure_id==unit_measure_id
            ).delete()
            
            # Commit the changes made in the session to the database.
            session.flush()
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            # If there's an IntegrityError, it's probably because the `unit_measure_id` is being referenced in another table. Raise a custom error.
            raise ChaliceViewError(
                f"Integrity error, probably unit measure id is being referenced in other table"
            )
        except Exception as e:
            raise ChaliceViewError(
                e
            )
        # If `deleted` is 0, it means that no rows were deleted. Raise not found error
        if deleted == 0:
            raise NotFoundError(
                'unit measure not found'
            )
        
        
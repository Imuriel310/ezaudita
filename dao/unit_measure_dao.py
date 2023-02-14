from sqlalchemy.orm.session import Session
from entity.unit_measure import UnitMeasure
from database.config import SessionLocal
from chalice import ChaliceViewError
from chalice import NotFoundError

def get_unit_measure_all() -> dict:
    with SessionLocal() as session:
        unit_measure_data = session.query(UnitMeasure).all()
        return unit_measure_data

def get_unit_measure_specific(unit_measure_id:int = None) -> dict:
    with SessionLocal() as session:
        unit_measure_data = session.query(UnitMeasure).filter(
            UnitMeasure.unit_measure_id==unit_measure_id
        ).first()
        return unit_measure_data
        
def save_unit_measure(name: str) -> dict:
    with SessionLocal() as session:
        new_unit_measure = UnitMeasure()
        new_unit_measure.name = name
        try:
            session.add(new_unit_measure)
            session.commit()
        except Exception as e:
            raise ChaliceViewError(
                e
            )
        return {'message': 'unit measure created'}

def update_unit_measure(unit_measure_new_name: str, unit_measure_id: int) -> dict:
    with SessionLocal() as session:
        unit_measure_row = session.query(UnitMeasure).filter(
            UnitMeasure.unit_measure_id==unit_measure_id
        ).first()
        if unit_measure_row is None:
            raise NotFoundError("unit measure not found")
        try:
            unit_measure_row.name = unit_measure_new_name
            session.flush()
            session.commit()
        except Exception as e:
            raise ChaliceViewError(
                e
            )
        return {'message': 'unit measure updated'}
        
        
from sqlalchemy.orm.session import Session
from entity.unit_measure import UnitMeasure
from database.config import SessionLocal

def get_unit_measure_all(unit_measure_id:int = None) -> object:
    with SessionLocal() as session:
        unit_measure_data = session.query(UnitMeasure).all()
        return unit_measure_data

def get_unit_measure_specific(unit_measure_id:int = None) -> object:
    with SessionLocal() as session:
        unit_measure_data = session.query(UnitMeasure).filter(
            UnitMeasure.unit_measure_id==unit_measure_id
        ).first()
        return unit_measure_data
        
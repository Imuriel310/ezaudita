from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from database.config import Base

class UnitMeasure(Base):
    __tablename__ = "unit_measure"
    __table_args__ = {"schema": "ezaudita"}
    
    unit_measure_id = Column(Integer, primary_key=True)
    name = Column(String)
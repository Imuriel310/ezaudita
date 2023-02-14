from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base
from .unit_measure import UnitMeasure

class Products(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "ezaudita"}
    
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Float)
    unit_measure_id = Column(ForeignKey('ezaudita.unit_measure.unit_measure_id'))
    
    unit_measure = relationship(UnitMeasure)
    
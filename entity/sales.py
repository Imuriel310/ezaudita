from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy.orm import relationship
from database.config import Base
from .unit_measure import UnitMeasure

class Sales(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "ezaudita"}
    
    sales_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    quantity = Column(Float)
    product_id = Column(ForeignKey('ezaudita.product.product_id'))
    
    unit_measure = relationship(UnitMeasure)
    
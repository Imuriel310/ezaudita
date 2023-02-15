from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy.orm import relationship
from database.config import Base
from .products import Products

class Sales(Base):
    __tablename__ = "sales"
    __table_args__ = {"schema": "ezaudita"}
    
    sales_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    quantity = Column(Integer)
    product_id = Column(ForeignKey('ezaudita.products.product_id'))
    
    product = relationship(Products)
    
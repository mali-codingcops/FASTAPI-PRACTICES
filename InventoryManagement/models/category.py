from ..databases import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
class Category(Base):
    
    __tablename__ = "Category"

    id = Column(String, primary_key=True, index= True)
    name = Column(String)

    product = relationship('Product', back_populates='category', cascade="all, delete-orphan")

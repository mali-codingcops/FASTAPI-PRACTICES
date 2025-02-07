from databases import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional
class Product(Base):
    
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    prodcut_name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    image_path = Column(String)
    category_id = Column(Integer, ForeignKey('Category.id'))
    category = relationship('Category', back_populates= 'product')

  
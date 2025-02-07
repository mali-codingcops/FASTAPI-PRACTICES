from databases import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
class Product(Base):
    
    __tablename__ = "Product"

    id = Column(String, primary_key=True, index= True)
    prodcut_name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('Category.id'))
    category = relationship('Category', back_populates= 'product')

  
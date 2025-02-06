from InventoryManagement.databases import Base
from sqlalchemy import Column, String, Integer

class Product(Base):
    
    __tablename__ = "Product"

    id = Column(String, primary_key=True, index= True)
    prodcut_name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    category_id = Column(Integer)
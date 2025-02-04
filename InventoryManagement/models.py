from .databases import Base
from sqlalchemy import String, Float, Column, ForeignKey, Integer

class Products(Base):
    
    __tablename__ = "Products"
    
    pro_id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    desc = Column(String)
    price =  Column(Float)
    stock = Column(Integer)
    
    #category_id : int

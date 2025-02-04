from pydantic import BaseModel

class Products(BaseModel):
    name: str
    desc: str
    price: float
    stock: int
    #category_id : int
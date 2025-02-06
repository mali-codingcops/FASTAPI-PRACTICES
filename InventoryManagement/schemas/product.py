from pydantic import BaseModel, field_validator

class ProductBase(BaseModel):
    
    prodcut_name : str
    price : int
    stock : int
    category_id : int

    @field_validator('prodcut_name')
    @classmethod
    def validate_product_name(cls, product_name):
        if not product_name:
            raise ValueError("Product Name Can't be Empty")
        return product_name
    @field_validator('price', 'stock')
    @classmethod
    def neg_value_validate(cls, value, field):
        if value < 0:
            raise ValueError(f"{field} Can't be a negative number")
        return value

class ProductCreate(ProductBase):
    pass
    
class Product(ProductBase):

    id : int
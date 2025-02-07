from sqlalchemy.orm import Session
from InventoryManagement.models.product import Product
from InventoryManagement.schemas.product import ProductCreate, ProductBase


def add_product(db: Session, product: ProductCreate):
    add_product = Product(**product.model_dump())
    db.add(add_product)
    db.commit()
    db.refresh(add_product)
    return add_product

def get_product(db: Session):
    return db.query(Product).all()

def get_product_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(product_id: int, product_detail: ProductBase, db: Session):
   
    db_product = db.query(Product).filter(Product.id == product_id).first()
    
    
    if not db_product:
        return None
    
    for key, value in product_detail.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
   
    return db_product

def delete_product(product_id: int, db: Session):

    delete_product = db.query(Product).filter(Product.id == product_id).first()

    if not delete_product:
        return None
    
    db.delete(delete_product)
    db.commit()

    return delete_product
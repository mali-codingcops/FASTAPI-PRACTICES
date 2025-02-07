from InventoryManagement.models.category import Category
from InventoryManagement.schemas.category import CategoryCreated
from sqlalchemy.orm import Session

def create_product(category: CategoryCreated, db: Session):
    
    create_product = Category(**category.model_dump())
    db.add(create_product)
    db.commit()
    db.refresh(create_product)
    return create_product

def get_category(db: Session):
    return db.query(Category).all()

def delete_category(category_id: int, db: Session):

    delete_category = db.query(Category).filter(Category.id == category_id).first()

    if not delete_category:
        return None
    
    db.delete(delete_category)
    db.commit()

    return delete_category

def update_category(category_id: int, update_category: CategoryCreated, db: Session):
    
    category = db.query(Category).filter(Category.id == category_id).first()

    if not update_category:
        return None
    
    for key, value in update_category.dict(exclude_unset=True).items():
        setattr(category, key, value)
    
    db.commit()
    db.refresh(category)

    return category
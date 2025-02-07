from fastapi import APIRouter, status, Depends, HTTPException
from ..schemas import category as category_schema
from ..curd import category as category_crud
from databases import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    tags= ['category']
)

@router.get("/get_category", response_model=List[category_schema.CategoryCreated], status_code=status.HTTP_200_OK)
def get_category(db: Session = Depends(get_db)):
    all_category = category_crud.get_category(db)
    if all_category is None:
        raise HTTPException(detail=f"Unable to get Category", status_code=status.HTTP_204_NO_CONTENT)
    return all_category

@router.post("/create_category", response_model=category_schema.CategoryCreated, status_code=status.HTTP_201_CREATED)
def create_category(category: category_schema.Category, db: Session = Depends(get_db)):
    create_category = category_crud.create_product(db=db, category=category)
    if create_category is None:
        raise HTTPException(detail="Unable to Add Product.", status_code=status.HTTP_304_NOT_MODIFIED)
    return create_category

@router.delete("/delete_category", response_model=str, status_code=status.HTTP_200_OK)
def delete_category(category_id, db: Session = Depends(get_db)):
    delete_category = category_crud.delete_category(category_id= category_id, db= db)
    if delete_category is None:
        raise HTTPException(detail=f"Unable to delete category with id {category_id}", status_code=status.HTTP_404_NOT_FOUND)
    return f"Successfully deleted the category with id {category_id}"

@router.put("/update_category", response_model=category_schema.CategoryCreated, status_code=status.HTTP_200_OK)
def update_category(category_id : int, update_category: category_schema.CategoryCreated, db: Session = Depends(get_db)):
    update_category = category_crud.update_category(category_id= category_id, update_category=update_category, db= db)
    if update_category is None:
        raise HTTPException(detail="Unable to update the category", status_code=status.HTTP_304_NOT_MODIFIED)
    return update_category

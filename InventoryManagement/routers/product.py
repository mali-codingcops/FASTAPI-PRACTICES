from fastapi import APIRouter, Depends, status, HTTPException
from databases import engine, get_db
from sqlalchemy.orm import Session
from ..curd import product as product_curd
from ..schemas import product as product_schemas
from typing import List

router = APIRouter(
    tags= ['Products']
)

@router.post("/products", response_model=product_schemas.ProductCreate, status_code=status.HTTP_201_CREATED)
def add_product(product: product_schemas.Product, db: Session = Depends(get_db)):
    add_product = product_curd.add_product(db=db, product=product)
    if add_product is None:
        raise HTTPException(detail="Unable to Add Product.", status_code=status.HTTP_304_NOT_MODIFIED)
    return add_product

@router.get("/get_products", response_model= List[product_schemas.ProductCreate], status_code = status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    all_products = product_curd.get_product(db= db)
    if not all_products:
        raise HTTPException(detail="No Product is found!", status_code=status.HTTP_204_NO_CONTENT)
    return all_products 

@router.get("/get_products/{product_id}", response_model=product_schemas.ProductBase, status_code=status.HTTP_200_OK)
def get_products_id(product_id, db: Session = Depends(get_db)):
    get_product = product_curd.get_product_id(product_id= product_id, db= db)
    if get_product is None:
        raise HTTPException(detail=f"No Product with id {product_id} exist", status_code=status.HTTP_404_NOT_FOUND)
    return get_product

@router.put("/update_product_detail", response_model=product_schemas.ProductBase, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product: product_schemas.ProductBase, db: Session = Depends(get_db)):
    update_product = product_curd.update_product(product_id = product_id, product_detail= product, db= db)
    if update_product is None:
        raise HTTPException(detail=f"Unable to update the Product Content with id {product.id}", status_code=status.HTTP_304_NOT_MODIFIED)
    return update_product

@router.delete("/delete_product", response_model=str, status_code=status.HTTP_200_OK)
def delete_product(product_id, db: Session = Depends(get_db)):
    delete_product = product_curd.delete_product(product_id = product_id, db= db)
    if not delete_product:
        raise HTTPException(detail=f"Unable to delete product with {product_id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return f"Product with id {product_id} is successfully deleted."
    
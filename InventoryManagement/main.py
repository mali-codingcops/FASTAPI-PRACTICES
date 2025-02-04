from fastapi import FastAPI, Depends
from . import schemas, models
from .databases import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.post("/add_product")
def add_product(request: schemas.Products, db: Session = Depends(get_db)):
    add_product = models.Products(name= request.name, desc= request.desc, price= request.price, stock= request.stock)
    db.add(add_product)
    db.commit()
    db.refresh(add_product)
    return add_product

@app.get("/get_all_product")
def get_all_product(db: Session = Depends(get_db)):
    all_product = db.query(models.Products).all()
    return all_product

@app.get("/get_product/{prod_id}")
def get_product_details(prod_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.pro_id == prod_id).first()
    return product

@app.get("/about")
def about():
    return {
        "data": {
        "project": "FASTAPI Paratices",
        "version": "0.0.1"
        }
    }
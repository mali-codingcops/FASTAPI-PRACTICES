from fastapi import FastAPI, Depends
from .databases import engine, get_db
from sqlalchemy.orm import Session
from .routers import product
from InventoryManagement import models


app = FastAPI()
models.product.Base.metadata.create_all(engine)
app.include_router(product.router)

@app.get("/about")
def about():
    return {
        "data": {
        "project": "FASTAPI Paratices",
        "version": "0.0.1"
        }
    }
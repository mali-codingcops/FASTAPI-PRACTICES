from fastapi import FastAPI, Depends
from databases import engine
from sqlalchemy.orm import Session
from InventoryManagement.routers import product, category
from InventoryManagement import models
import uvicorn

app = FastAPI()
models.product.Base.metadata.create_all(engine)
app.include_router(product.router)
app.include_router(category.router)

@app.get("/about")
def about():
    return {
        "data": {
        "project": "FASTAPI Paratices",
        "version": "0.0.1"
        }
    }

if __name__ == "__main__":
    
    uvicorn.run(app=app, host='127.0.0.1', port=8080)
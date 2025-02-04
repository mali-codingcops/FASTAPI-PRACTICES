from fastapi import FastAPI


app = FastAPI()


@app.get("/about")
def about():
    return {
        "data": {
        "project": "FASTAPI Paratices",
        "version": "0.0.1"
        }
    }

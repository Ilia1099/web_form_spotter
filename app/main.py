from fastapi import FastAPI
from app.api.routes import spot_form
import sys

app = FastAPI()
app.include_router(spot_form.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

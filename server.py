from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello Machine Learning"}

@app.post("/predict")
async def get_predict(types: Annotated[list, Form()], location: Annotated[str, Form()]):
  return {
    "types": types,
    "message": "Request Filled"
  }
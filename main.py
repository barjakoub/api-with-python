from typing import Annotated
from fastapi import FastAPI, Form
from barjakoub.generate_input import Input
from barjakoub.gmaps_api import nearby_search
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello Machine Learning"}

@app.post("/predict")
async def get_predict(btypes: Annotated[list, Form()], latitude: Annotated[float, Form()], longitude: Annotated[float, Form()]):
  # structuring request body
  input = {
    "btypes": btypes,
    "latitude": latitude,
    "longitude": longitude
  }
  print(btypes)
  # create instance
  juki = Input(input)
  headers_nya = Input.create_headers_req()
  body_nya = juki.create_body_req()
  # make request and send back to user
  resp = nearby_search(headers=headers_nya, body=body_nya)
  return resp

@app.get('/machinelearning')
async def sapa_ml():
  return Input.ml_members()
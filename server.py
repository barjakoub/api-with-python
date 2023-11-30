from typing import Annotated
from fastapi import FastAPI, Form
import sys

sys.path.append('C:\\Learning Programming\\Python Learning\\demo-thurs-nov-30\\class')
sys.path.append('C:\\Learning Programming\\Python Learning\\demo-thurs-nov-30\\helper')

from user_preference import Preference
from gmaps_api import nearby_search

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
  # create object
  juki = Preference(input)
  headers_nya = Preference.create_headers_req()
  body_nya = juki.create_body_req()
  # make request and send back to user
  resp = nearby_search(headers=headers_nya, body=body_nya)
  return resp

@app.get('/machinelearning')
async def sapa_ml():
  return Preference.ml_members()
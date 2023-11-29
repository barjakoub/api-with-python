import requests
import json

base_url = 'https://places.googleapis.com/v1/places:searchNearby'

def nearby_search(headers, body):
  # parameter data harus menggunakan "json.dumps()" karena gmaps api hanya menerima request Content-Type "application/json"
  resp = requests.post(url=base_url, headers=headers, data=json.dumps(body))
  parse = resp.json()
  return parse

def call_ML(name):
  return f"Hi, {name}"
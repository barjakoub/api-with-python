from barjakoub.generate_input import Input
from barjakoub.gmaps_api import nearby_search

'''
    Supported place types, go to the link https://developers.google.com/maps/documentation/places/web-service/place-types
'''
static_data = {
  'btypes': 'LIST_OF_TYPES',
  'longitude': 'FLOATING_NUMBER',
  'latitude': 'FLOATING_NUMBER'
}

juki_parah = Input(static_data)

resp = nearby_search(headers=Input.create_headers_req(), body=juki_parah.create_body_req())

print(resp)
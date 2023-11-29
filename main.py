import sys
# add module directory to sys.path
'''
  sesuaikan directory folder "class" dan "helper" sesuai dengan komputer/laptop kalian masing-masing
  cara termudah:
    1. buka folder "class" atau "helper"
    2. klik kanan pada module "user_preference.py" atau "gmaps_api.py"
    3. klik "copy path" dan pasti ke dalam "sys.path" dibawah ini
    4. pastikan tanda slash ada 2 "\\", bukan 1 "\" 
'''
# direktori folder class
sys.path.append('C:\\Learning Programming\\Python Learning\\demo-thurs-nov-30\\helper')
# direktori folder helper
sys.path.append('C:\\Learning Programming\\Python Learning\\demo-thurs-nov-30\\class')
# print(sys.path)
# importing function and class
from gmaps_api import call_ML, nearby_search
from user_preference import Preference

'''
  anda dapat mengisi data berikut sesuai yang anda inginkan. tapi ingat, untuk "btypes" nilai harus sesuai dengan tipe yang telah disediakan oleh google maps platform, more detailed https://developers.google.com/maps/documentation/places/web-service/place-types
'''
static_input = {
  "btypes": ['cafe', 'bank'],
  "longitude": 112.788445,
  "latitude": -7.290298
}

print(Preference.greet_to_ML('Merissa, Qarin, dan Salomo'))

# create object instance
ml_division = Preference(static_input)

# create body request from instance
body = ml_division.create_body_req()

# create headers using Preference static method
headers = Preference.create_headers_req()
print(headers)

# perform nearby search
response = nearby_search(headers=headers, body=body)
print(response)

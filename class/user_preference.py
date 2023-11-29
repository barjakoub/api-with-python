class Preference:
  source = 'This from Fatkhur Rozak'
  def __init__(self, input):
    self.types = input['btypes']
    self.longitude = input['longitude']
    self.latitude = input['latitude']
  
  def create_body_req(self):
    return {
      "includedTypes": self.types,
      "locationRestriction": {
        "circle": {
          "center": {
            "latitude": self.latitude,
            "longitude": self.longitude
          },
          # radius bisa kalian sesuaikan
          "radius": 500.0
        }
      }
    }
  
  @classmethod
  def Author(cls):
    return cls.source
  
  @staticmethod
  def greet_to_ML(name):
    return f'Hi, Kak {name}'
  
  '''
      FieldMask bisa anda sesuaikan di https://developers.google.com/maps/documentation/places/web-service/nearby-search#fieldmask
      
      NOTE: minta api key pada Fatkhur yaa
  '''
  def create_headers_req():
    return {
      'Content-Type': 'application/json',
      'X-Goog-Api-Key': 'MINTA_PADA_FATKHUR_ROZAK_KEY_NYA',
      'X-Goog-FieldMask': 'places.displayName,places.rating,places.userRatingCount,places.priceLevel'
    }
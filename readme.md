### Samples Code for ML Division
#### Capstone Team ID : **CH2-PS514**
Key Point
- Make requests to Google Maps Platform (Nearby Search)
- Create simple APIs to handle requests

### Pre-Requirements
| Api Key |
|---------|
| direct message to Fatkhur|

> Please do the steps listed in the modules.

### `barjakoub` Package
To create an instance of the `Input` class, you must pass an argument like shown below:
```python
  static_data = {
    "btypes": <list_of_types>,
    "latitude": <floating_number>,
    "longitude": <floating_number>
  }

  instance = Input(static_data)
```
Class `Input` concists of the following:

- **`@staticmethod`**
  - `greet_to_ML(name)`
    
    This method returns `str` "Hi, Kak" followed by **`name`** argument.

  - `ml_members()`

    This method returns the list name of Machine Learning members.

  - `create_headers_req()`

    This method returns a dictionary to generate the required request `headers`.
    ```python
      {
        'Content-Type': <request-content-type>,
        'X-Goog-Api-Key': <gmaps-api-key>,
        'X-Goog-FieldMask': <request-data-fields>
      }
    ```
- **`@classmethod`**
  - `Author()`

    This class method returns the name of this author: `str`

- **`instance_method`**
  - `create_body_req()`

    This method returns a dictionary to generate the required request `body` based on `Preference` instantiation data.
    ```python
      {
        "includedTypes": <user-types-in-list>,
        "locationRestriction": {
          "circle": {
            "center": {
              "latitude": <floating-number>,
              "longitude": <floating-number>
            },
            "radius": 500.0
        }
      }
      }
    ```
___
**`gmaps_api`** module provides method to perform Google Maps Platform requests
- **`nearby_search(headers, body)`**
  
  This method required two argument `headers` and `body`. You can simplify pass `headers` parameter by generating headers with `Preference.create_headers_req()` and pass the `body` parameter by calling the instance method **`instance_name.create_body_req()`**. This will generate a request body based on instance data.

  Then, this method returns the results of places near from user's location.
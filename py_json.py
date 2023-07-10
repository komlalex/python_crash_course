# JSON is commonly used with data APIs. Here is how to parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"firstname": "Alex", "lastname": "Komla", "age": 25}'


# Parse to dictionary
user = json.loads(userJSON)

print(user)
print(user["firstname"]) # Alex


# How to parse a dictionary into a json
car = {
    "name": "Toyota",
    "model": "TYT 77",
    "year": 2023
}

carJSON = json.dumps(car)
print(carJSON)
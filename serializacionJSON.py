import json

# Convert from JSON to Python:

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#------------------------------------------------------------------------------------------

# Convert from Python to JSON:

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#------------------------------------------------------------------------------------------------

# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Parameters to make it easy to read

#Using indent to define the number of indents
print(json.dumps(x, indent=4))

#Define separators to change the default ("," , ":")
print(json.dumps(x, indent=4, separators=("." , "=")))

#Order the result
print(json.dumps(x, indent=4, sort_keys=True))

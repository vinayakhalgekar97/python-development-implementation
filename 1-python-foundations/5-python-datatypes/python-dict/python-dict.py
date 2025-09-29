"""Python Dictionary"""

"""How to Create a Dictionary"""
person = {
    "name": "Vinayak Halgekar",
    "age": 27,
    "Designation": "Software Developer"
}

car = dict(name = "Toyota", color = "red", tyres=4) # create dictionary using dict() constructor

print(person)
print(car)

"""Accessing Dictionary Items"""
print(person["name"])
print(car.get('name'))

"""Adding and Updating Dictionary Items"""
person["height"] = 162
person["weight"] = 79

car["name"] = "Maruti"

print(person)
print(car)

"""Iterating Through a Dictionary"""
# Iterate over key
for key in person:
    print(person[key])

# Iterate over value
for value in person.values():
    print(value)

# Iterate over key and value
for key, value in person.items():
    print(key, value)

"""Nested Dictionaries """
student = {}
student["Vinayak"] = {
    "age": 27,
    "grade": "A+"
}
student["Rohan"] = {
    "age": 28,
    "grade": "A"
}
print(student)
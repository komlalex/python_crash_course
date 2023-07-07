# A Dictionary is a collection which is unordered, changebale and indexed. No duplicate members

# Create a dict
person = {
    "first_name": "Alexander",
    "last_name": "Kunyelewosi",
    "age": 25
}
print(person, type(person))

# Using the dict contructor
person2 = dict(name="John Doe", age=55)
print(person2, type(person2))

# Get value
print(person["age"]) #25
print(person.get("last_name"))

# Add key value
person["phone"] = "555-333-222"
print(person)

#Get keys
print(person.keys())

#Get items
print(person.items())

# Copy dict
person_copy = person.copy()

person_copy["isMarried"] = True
print(person_copy)

# Remove an item
del person["age"]
person.pop("phone")
print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person_copy)) # 5

#List of dictionaries
people = [
    {"name": "Alex", "age": 25},
    {"name": "Vivian", "age": 26},
    {"name": "Esther", "age": 23}
]

print(people, type(people))
print(people[2].get("name")) #Esther
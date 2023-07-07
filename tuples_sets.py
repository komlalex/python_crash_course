# A TUPLE is a collection which is ordered and unchangeable. Allows duplicate members

#Create a tuple
fruits = ("Apples", "Oranges", "Grapes")
fruits2 = tuple(("Apples", "Oranges", "Grapes"))

print(fruits, fruits2)

#If the tuple has only one member, remember to leave a trailing comma, else it will be casted to a string
fruits3 = ("Pineapple",)

print(fruits3, type(fruits3))

# Get a sigle value
print(fruits[1]) # Oranges

# Can't change a value
#fruits[0] = "Mango" #error

# Delete tuple
del fruits2
#print(fruits2)

# Get length
print(len(fruits))



# A SET is a collection which is unordered and unindexed. No duplicate members

#Create a set
pets = {"Cat", "Dog", "Monkey"}
pets2 = set(("Cat", "Dog", "Monkey", "Cat", "Monkey"))
print(pets, pets2)
print(type(pets), type(pets2))

# Check if i set
print("Snake" in pets) # False
 
#Add to set
pets.add("Goldfish")
print(pets)

# Remove from set
pets.remove("Monkey")
print(pets)

# Clear the whole set
pets.clear()
print(pets)

# Delete the set
del pets
#print(pets) #NameError



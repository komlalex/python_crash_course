# A list is a collection which is ordered and changeable. It also allows duplicate members

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Use a contructor
numbers2 = list((6, 7, 8, 9, 0))

# Get a single value
print(fruits[1]) # Oranges

# Get length
print(len(fruits)) # 4


# Append to the list
fruits.append("Mangoes")
print(fruits) # ['Apples', 'Oranges', 'Grapes', 'Pears']

# Remove from list
fruits.remove("Grapes")
print(fruits) # ['Apples', 'Oranges', 'Pears', 'Mangoes']

# Change a value
fruits[2] = "Dragonfruit"

# Insert into a specific postion
fruits.insert(2, "Figs")
print(fruits)

# Remove with pop
fruits.pop(0)
print(fruits)
# Reverse the list
fruits.reverse()
print(fruits)

# Sort 
fruits.sort()
print(fruits, "Sorted")

# Reverse sort
fruits.sort(reverse=True)
print(fruits, "Reverse sorted")

# 
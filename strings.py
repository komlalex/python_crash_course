#Strings in python are surrounded by either single or double quotation marks

name = "Alex"
age = 25

#Concatenate 
#Remember only strings can be concatenated
print("Hello, my name is " + name + " and I am " + str(age) + " years old")

#String Formatting
#Postional arguments
print("My name is {name} and I am {age} years old".format(name=name, age=age))

#F-Strings
print(f"Hello, my name is {name}. I am {age} years of age")

# Capitalize 
s = "komla"
t = "KOMLA"
v = "Hello world"
print(s.capitalize()) #Komla

# Make all uppercase
print(s.upper()) #KOMLA

#Make all lowercase
print(t.lower()) #komla

# Swap case
print(s.swapcase()) #KOMLA

# Get Length
print(len(s)) # 5

# Replace
print(v.replace("world", "Collins!")) # Hello Collins!

#Count
l = "l"
print(v.count(l)) # 3

# Ends with
print(s.endswith("d")) # False

# Starts with
print(s.startswith("k")) # True

# Split into a list
print(v.split("l")) # ['He', '', 'o wor', 'd']

# Find Postion
print(s.find("o")) # 1
print(s.find("5")) # -1

# Is Alphanumeric
print(s.isalnum()) #True

# Is all alphabets
print(s.isalpha()) #True

# Is all numeric
print(s.isnumeric()) # False

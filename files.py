# Python has functions for creating, reading, updating and deleting files

# Open a file
myFile = open("myfile.txt", 'w')


# Get info
print(f"Name: {myFile.name}")
print(f"Is Closed: {myFile.closed}")
print(f"Opening Mode: {myFile.mode}")


# Write to file
myFile.write("I love python ")
myFile.write("and JavaScript.")
myFile.close()

print(myFile.closed)

# Append to file
myFile = open("myfile.txt", "a")
print(myFile.mode)
myFile.write(" These are the two most used languages.")
myFile.close()

# Read from a file
myFile = open("myfile.txt", "r+")
text = myFile.read(100)
print(text)
myFile.close()

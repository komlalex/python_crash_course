# A fuction is a block of code which only runs when it is called. In Python, we do not use curly brackets. 
# We use indetation with tabs or spaces

# Create a function
def sayHello(name = "Client"):
    print(f"Hello {name}")

sayHello("Alex")

# Return values
def getSum(num1, num2):
    total= num1 + num2
    return total

num = getSum(20, 13)
print(num) #33

# A lambda is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions.

getSum = lambda num1, num2: num1 + num2 

print(getSum(7,7)) #14

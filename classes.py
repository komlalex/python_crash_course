#  A class is a blueprint for creating an object. An object has properties and methods (functions) associated with it.
# Almost everything in Python is an object

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def greeting(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years of age."
    
    def has_birthday(self): 
        self.age += 1

    def setbalance(self, balance): 
        self.balance = balance


# Initialize user object
alex = User("Komla Alex", "kunalex@hotmail.com", 23)

print(type(alex))
print(alex.age)

alex.has_birthday()
print(alex.greeting())


# Extending classes
class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f"Hello I am {self.name}, I am {self.age} and my balance is {self.balance}"

# Initialize
alice = Customer("Alice Wonderland", "alicew@gmail.com", 19)

alice.set_balance(45)
print(alice.greeting())

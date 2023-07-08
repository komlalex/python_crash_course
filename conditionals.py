# If/Else conditions are used to decide to do something based on something being true or false
x = 5
y = 5

# simple if
if x > y:
    print(f"{x} is greater than {y}")

# If else
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")

# elif
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else: 
    print(f"{y} is greater than {x}")


# Nested if statements
a = 70
b = 7
if b > a:
    if a <= b:
        print(f"{a} is less than or equal to {b}")

# Comparison operators (==, !=, <, >, <=, >=) are used to compare values

# Logical operators (and, or, not) are used to combine coditional statements
#and
if a < 15 and a >= 4:
    print(f"{a} is less than 15, and greater than or equal to 4")

#or
if a < 15 or a >= 12: 
    print(f"{a} is less than 15, or greater than or equal to 12")

#not
if not(a == b):
    print(f"{a} is not equal to {b}")
# Membership operators (not, not in) are used to if a sequence is presented in an object
numbers = [1,2,3,4,7,5,]

#in
if 1 in numbers:
    print(1 in numbers)

# not in
if 19 not in numbers:
    print(19 not in numbers)

# Identiy Operators (is, is not) are used to compare objects not if they are equal, but if 
# they are actually the same object with the same memory location

# is
if a is b: 
    print(a is b)

if a is not b: 
    print(f"a is not b")
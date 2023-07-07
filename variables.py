# A variable is a container for a value, which can be of various types
#x = 10 #int
#y = 2.5 #float
#name = "Alex" #string
#is_good = True #boolean

#Multiple assignment
x, y, name, is_good = (10, 2.5, "John", True)

#Print
print(x, name)

#Basic maths
a = 700 
b = 301
print(a  + b) 

#Checking type
print (type(x)) # <class 'int'>
print (type (y)) # <class 'float'>
 
#Casting
x = str(x)
print(type(x)) # <class 'str'>
y = float(x)
print(y) # 10.0
print(int(y)) #10
print(bool(name)) #True
print (bool(0)) #False
print(bool("")) #False
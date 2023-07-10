# A module is basically a file containing a set of functions to include in your application
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# CORE MODULES
import datetime
from datetime import date
import time
from time import time

#today = datetime.date.today()
today = date.today()
print(today)

timestamp = time()
print(timestamp)

# PIP MODULES

# CUSTOM MODULE
from validate import validate_email
email = "test@hotmail.com"

if validate_email(email):
    print('Email is valid')
else:
    print('Email not valid')


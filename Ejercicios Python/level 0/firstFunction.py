import random

age= random.randrange(1,99)
if (age<18):
    print (str(age) + " Access denied")
else:
    print (str(age) + " Access Allowed")
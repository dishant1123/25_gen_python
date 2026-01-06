# function  : 
"""
4 type  : 

1. no arg  no return  
2. no arg  with return
3. with arg  no return
4. with arg  with return
"""

# 1 : 

"""def add():
    a=10 
    b=90 
    c=a+b 
    print(c)
add()
"""

#3 : 

"""
def add(a,b): 
    c=a+b 
    print(c)
add(12,56)
add(89,56)
"""
# 2 : 

"""def add():
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a+b 
    return c
print(add())
"""
# 4 :
"""def add(a,b) :
    c=a+b 
    return c 
print(add(12,45))
print(add(120,450))
"""

# *args : it is take only numreic value . 

"""def add(a,b):
    c=a+b
    print(c)
add(12,67,67)
"""
# ex :1 
"""def add(*args):
    return sum(args)
print(add(1,2,3,4,5,6,7,8,44,56,34,23,67.89))
"""
# ex :2 
"""def addition(*x):
    sum =0 
    for i in x : 
        sum =sum +i 
    print(sum)
addition(112,34,55,66,889)
"""

# **kwargs : it is take key value as args.

"""
def d1(**kargs):
    for i  , j in kargs.items():
        print(f"{i} : {j}")
d1(name="moksh" , age=20 , gender="male")
"""

# local variable :
"""def x(): 
    a=90  #  a local variable ==> within function accessible 
    print(a)
x()
# print(a)  # not accessible outside the function  bcz of local variable. 
"""

# global variable :

"""x=100 
def y(): 
    print(x)  # global variable 
y()
print(x)  # accessible outside the function bcz of global variable
"""

# modify the  global variable using global keyword. 

"""
x=100 
def y():
    global x 
    x=90 
    print(x)
y() 
print(x)
"""

"""
task  :1 

ROYAL KID BANK 

1. username , password create  
2. options :
    1. login  ==> compulsory   ==>successfull   ===> ac 25000 deposit 
    2. deposit 
    3. withdraw  ==> min 10000 rs . 
    4. check balance 
    5. exit 

"""
# list  slicing :

"""l1=[1,2,3,4] 
print(l1)
"""
l2 =[[1,2,3],
     [30,4,8],
     [5,6,90]]

print(l2)
"""for i in  l2 :
    print(i)
   """ 
"""
[1, 2]  (0,0) 1  (0,1)2 
[3, 4]  (1,0) 3  (1,1)4
[5, 6]  (2,0) 5  (2,1)6
"""  
"""print(l2[0])
print(l2[0][0])
print(l2[1][1])
print(l2[0] [ : :-1])
print(l2[1] [ : :1])
print(l2[1] [ : :-2])
print(l2[1] [-2])
print(l2[2] [0 :3 :2])

print(l2[0] [ :])
"""

# task  :1 
# l2 =[[1,2],[0,-4],[5,6]]

# output : [0,-4],[1,2],[5,6]

# function  type  :
"""
1. no arg  no return
2. no arg  with return
3. with arg  no return
4. with arg  with return
"""
#1 : 
"""
def add():   # add name of function
     a=10 
     b=90    # function intialization
     c=a+b
     print(c)
add()
"""     

# 3 : with arg  no return

"""def add(a,b):
     c=a+b 
     print(c)
     
a=int(input("enter a : "))
b=int(input("enter b : "))
add(a,b)
c=int(input("enter c : "))
d=int(input("enter d : "))
add(c,d)
"""

# no arg  with return  : 
"""
def add():
     a=int(input("enter a : "))
     b=int(input("enter b : "))
     c=a+b 
     return c 
print(add())
"""
# with arg  with return  :

"""def add(a,b):
     c=a+b 
     return c 
a=int(input("enter a : "))
b=int(input("enter b : "))
print(add(a,b))
"""

# *arg : only take numreic value .

"""def add(*args):
     return sum(args)
print(add(1,2,3,5,6,7,3,4,555,6,7,12.67))
"""
"""def add(*x):
     sum =0 
     for i in x : 
          sum =sum +i 
     print(sum)
add(1,2,3,5,6,7,3,4,555,6,7,12.67)
"""

# **kwargs : take key value pair as args.

"""def d1(**kwargs):
     for  i , j in kwargs.items():
          print(i,j)
          
d1(name="moksh" , age=20 , gender="male")

"""

#local variable :

"""def x ():
     a=100   # a local variable ==> within function accessible
     print(a)
x()
# print(a)  # not accessible outside the function  bcz of local variable.
"""

#global variable :

"""a=100 
def x():
     print(a)
x()
print(a)
"""
# modify the  global variable using global keyword. 

a=120 
def x():
     global a 
     a=890 
     print(a)
x()
print(a)
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

def add(a,b):
     c=a+b 
     return c 
a=int(input("enter a : "))
b=int(input("enter b : "))
print(add(a,b))
     
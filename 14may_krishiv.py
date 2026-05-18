# pip install  numpy  
# numpy  :   

import  numpy as np 

# 1 d array : 

"""a = np.array([1,2,3,4,5,6,7,8])
print(a)
print(type(a))
"""
# 2 d array : 
"""
b= np.array([[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]) 
print(b)
"""
# 3 d array  : 

"""
c= np.array([[[1,2,3],[4,5,6],[7,8,9]]]) 
print(c)
d= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d)
"""

# dimention  ,size : ,shape

# a = np.array([1,2,3,4,5,6,7,8])
"""
print(a)
print(type(a))
print(a.ndim)   # number  of  dimension:1 
print(a.size)   # number  of  elements  :8 
print(a.shape)  # shape of array :8 rows 

c= np.array([[[1,2,3],[4,5,6],[7,8,9]]]) 
print(c)
print(c.ndim)   # number  of  dimension:3
print(c.size)   # number  of  elements  :1
print(c.shape)  # shape of array :1 rows
"""
"""a1 = a.astype(float)
print(a1)
print(a1.itemsize)
"""

# c= np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int) 
# c= np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float) 
# c= np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=str) 
# c= np.array([[1,2,0],[0,5,6],[7,8,9]],dtype=bool) 
# c= np.array([[1,2,0],[0,5,6],[7,8,9]],dtype=complex) 
# print(c)


# create  one  matrix : 
"""
a=np.ones((4,3),dtype=int)
print(a)
"""
# create  zero  matrix : 

"""
a=np.zeros((4,3),dtype=int)
a=np.zeros((4,3),dtype=str)
print(a)
"""

# diagonal  matrix :

"""
a= np.diag([1,3,6])
print(a)
"""
# identity  matrix :

"""
b= np.eye(4,4).astype(int)
print(b)
"""

# arange function  : 

"""a= np.arange(10)
print(a)

b=np.arange(1,20,2)  # start stop  step   ==> last number excluded 
print(b)
"""
# formula  linespace :  stop -start / step-1 
# linspace  function  : 

"""a= np.linspace(1,12 ,10)
print(a)
"""

# reshape  :
"""a= np.arange(1,10)
a= np.arange(1,10).reshape(3,3)
a= np.arange(1,19).reshape(2,3,3)  # 3 rows 3 columns 2 number of  matrix

a=np.arange(1,33,dtype=float)
a= a.reshape(2,2,2,4)  # 2 matrix * 2 matrix *2 row *4 col

a=np.arange(0,20).reshape(2,2,5)
print(a)
"""

#ravel : it replace the memory . 

"""x=np.arange(1,10).reshape(3,3)
print("original array :\n",x)

x1 =x.ravel()
print("ravelled array :\n",x1)

x[0,0] =55
print("original array :\n",x)
print("ravelled array :\n",x1)
"""
# flatten  :create a new memory. 

"""x=np.arange(1,10).reshape(3,3)
print("original array :\n",x)

x1 =x.flatten()
print("flatten array :\n",x1)

x[0,0] =55
print("original array :\n",x)
print("flatten array :\n",x1)
"""

# traspose  :

"""
a= np.arange(1,10).reshape(3,3)
print(a)
result =np.transpose(a)
print(result)
print(a.T)
"""
# mathematical  function  :

"""
a= np.arange(1,10).reshape(3,3)
b= np.arange(11,20).reshape(3,3)

print(a)
print(b)
# print(a+b)
# print(a-b)
# print(a*b)  # not  matrxi multiplication
# print(a/b)

# matrix  multiplication  :

# result =np.matmul(a,b)
result =a.dot(b)
print(result)
"""
# statistical function   : mean midian std var 

# a= np.arange(1,10).reshape(3,3)
"""a= np.array([[1,2,30],[47,5,6],[7,80,9]])

print(a)
print(a.mean())
print(a.std())
print(a.var())
"""
# axis  : 
"""
axis = 1  row  wise 
axis = 0  column  wise
"""

"""print(a.sum(axis=1))   # row wise
print(a.sum(axis=0))   # column wise

print(a.max())
print(a.max(axis=1))   # row wise
print(a.argmax(axis=0))   #  col wise  print  index number of  max value 

print(a.min())
print(a.min(axis=1))   # row wise
print(a.argmin(axis=0))   #  col wise  print  index number of  min 

print(a.argsort(axis=1))   # row wise
print(a.argsort(axis=0))   #  col wise  print  index number of  min
"""
# random , slicing   , hstack vstack  : 

import  random  as r 

"""
a = np.random.random((3,3))  # 0 -1 value 
print(a)
"""
"""b = np.random.randint(low=-10, high =20,size=12).reshape(3,4)
print(b)
"""
"""c =np.random.sample(5)  # 0-1 
print(c)

d= np.random.choice(a=range(1,20),size=5)  # random choice
print(d)
"""

# where :  condition  

"""a= np.random.randint(low =-10, high =20,size=9).reshape(3,3)
print(a)

result =np.where(a>10)
print(result)
"""

# slicing  : 
a = np.array([1,2,3,4,5,6,7,8])
# print(a[0])
# print(a[2 :4])
# print(a[2 :6 :2])

b =np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
    
])
print(b)
print(b[0])
print(b[2:4])
print(b[2:5, 1:3])  # 2:5 row wise  1 :3 col wise 

"""
task :1 using  np.zeros , ones and slicing

1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1

task :2 take  5*5 matrix and  print  this  only : 
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
    
output  : [[11,12],
           [16,17]]
           
task :3  
    output  : [[2,8,14,20]]

task :4 
    output  :[[4,5],
              [19,20],
              [24,25]]
"""


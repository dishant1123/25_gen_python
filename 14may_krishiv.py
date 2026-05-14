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
# a= np.arange(1,10)
# a= np.arange(1,10).reshape(3,3)
# a= np.arange(1,19).reshape(2,3,3)  # 3 rows 3 columns 2 number of  matrix

# a=np.arange(1,33,dtype=float)
# a= a.reshape(2,2,2,4)  # 2 matrix * 2 matrix *2 row *4 col

a=np.arange(0,20).reshape(2,2,5)
print(a)



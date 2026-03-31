"""
numpy  : 
1. array , matrix ,vector  
2. support for complex number, large number
3. use mathematical function like algebraic operation, random number generation
4. less memory usage
5.fast  processing

"""
# install numpy : pip install numpy  

import numpy as np 

# ex :1    1 d array
"""a= np.array([1,2,3,4,5,6])
print(a)
print(type(a))
"""
# 2 d array  : 
"""
b= np.array([[1,2,3],[3,4,5],[6,7,8]])
print(b)
"""
# 3 d array  :

"""c= np.array([[[1,2,3],[3,4,5],[6,7,8]]])
print(c)
"""

# find shape , dimension ,size : 
"""a= np.array([1,2,3,4,5,6])
print(a)
print(a.shape)  # row  , col 
print(a.ndim)  # number of dimension
print(a.size)  # total number of element
print(a.itemsize)  # size of each element

a1=a.astype("float64")
print(a1)
print(a1.itemsize)

b= np.array([[1,2,3],[3,4,5],[6,7,8]])
print(b)
print(b.shape)
print(b.ndim)
print(b.size)

three1 =np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])

print(three1)
print(three1.shape)
"""
# change in data type  :

"""
x=np.array([[1,2,3],[13,14,15],[6,7,8]])
x=np.array([[1,2,3],[13,14,15],[6,7,8]],dtype="float")
x=np.array([[1,2,3],[13,14,15],[6,7,8]],dtype="str")
x=np.array([[1,2,3],[0,14,0],[6,7,0]],dtype="bool")
x=np.array([[1,2,3],[13,14,15],[6,7,8]],dtype="complex")

print(x)
"""

# create ones matrix and change data type  : 

"""ones = np.ones((4,3))
ones = np.ones((4,3),dtype="int")
ones = np.ones((4,3),dtype="str")
ones = np.ones((4,3),dtype="bool")
ones = np.ones((4,3),dtype="complex")

print(ones)
"""

# create zeros matrix and change data type  :

"""zeros = np.zeros((4,3))
zeros = np.zeros((4,3),dtype="int")
zeros = np.zeros((4,3),dtype="str")
zeros = np.zeros((4,3),dtype="bool")
zeros = np.zeros((4,3),dtype="complex")

print(zeros)
"""

# diagonal matrix  : .diag()

"""a=np.diag([1,3,6,2,9])
print(a)
"""
# identity matrix  : eye()

# a=np.eye(3)
# print(a)
# b=np.eye(4,4)
# print(b)

c=np.eye(3,4)
print(c)

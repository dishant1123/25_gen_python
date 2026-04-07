import numpy as np

# arange  function  : 


"""a=np.arange(10)  # [1,2,3,4,5,6,7,8,9]
print(a)

b= np.arange(1,10,2)  # start ,stop ,step
print(b)
"""
# linspace  function  :

"""a= np.linspace(1,12 ,10)
print(a)
# stop -start / step    12 -1 /10  ==> 11 /10 ==> 1.1  2.2 -1 ==>1.1

"""

# reshape  of  matrix : 

"""
    # a=np.arange(1,19).reshape(3,3,2)  # 3d  3 row 2 col 
a=np.arange(1,19).reshape(9,2)  # 3d  3 row 2 col 
# print(a)

x=np.arange(1,33,dtype=float)
# print(x)

print(x.reshape(2,2,2,4))  # 2 mat * 2 mat *2 row *4 col 

x=np.arange(0,20).reshape(2,2,5)
print(x)
print(x.ndim)
"""

# ravel ,flatten  function  :
"""
ravel and flatten are dimention reduction techniques which convert any dimention it to one dimention. 
"""
# ravel :

"""x=np.arange(1,10).reshape(3,3)
print(x)
x1= x.ravel()  # it replace the memory location of the array. 
print(x1)

x[0,0] =55
print(x)
print(x1)
"""

# flatten : 


"""x=np.arange(1,10).reshape(3,3)
# print(x)
x1=x.flatten() #it create a new memory . 
# print(x1)

x[0,0] =55
print(x)
print(x1)

"""
# transpose  function  :

"""a=np.arange(1,5).reshape(2,2)
print(a)
print(a.T)  # transpose
print(a.transpose())

b=np.arange(1,10).reshape(3,3)
print(b)
print(b.T)
print(b.transpose())
"""
# maths  function  :

"""a=np.arange(11,20).reshape(3,3)
b=np.arange(1,10).reshape(3,3)

print(a)
print(b)

print(a+b)
print(a-b)
print(a*b)  # not matrix multiplication
print(a/b)

# matrix   multiplication  :
print(np.dot(a,b))

"""

# statistics  function  :
"""
axis =0   col wise 
axis =1   row wise
"""


x=np.array([[4,8,1],[9,5,3],[11,5,7]])
print(x)
# print(x.sum(axis=0))
# print(x.min())
# print(x.max())
# print(x.mean())

# print(x.argmax())  # return the index of the max value
# print(x.argmin())  # return the index of the min value
# print(x.argmin(axis=0)) # [0,1,0]
# print(x.argmin(axis=1)) # [2,2,1 ]
# print(x.argmax(axis=0)) 
print(x.argmax(axis=1)) 

# print(x.std())



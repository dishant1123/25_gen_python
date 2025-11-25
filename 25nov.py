# tuple  : immutable sequence of element .  ==> not changes  in tuple.

"""t1=(1,2,3,4,5,6,"krishiv","moksh",True,8j,67.89)
print(t1)
print(type(t1))

t2= 23,45,68,"modi"
print(t2)
print(type(t2))

t3=23,"lsfnak"
print(t3)
print(type(t3))
"""

# built in function  :  len min max sorted sum 

"""
t1=(12,2,3,4,5,67.89)

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc 
print(sorted(t1,reverse=True))  # asc to desc 
print(sum(t1))
"""

# slicing  :

'''
t1=(12,2,3,4,5,67.89,99,77,44,22,11,"krishiv","moksh",True,8j,67.89)

"""t1[2] ="moksh"
print(t1)  # bcz  of tupel is immutable . 
"""

print(t1[5])
print(t1[2:6])
print(t1[:6])
print(t1[2:])
print(t1[-2: ])
print(t1[-8: -2 : 2 ])
print(t1[:  : 2 ])
print(t1[:  : -1 ])
'''

# method  : 

"""t1=(12,2,3,4,5,67.89,99,77,44,22,11,67.89,2)

# print(t1.count(2))
print(t1.index(2))
print(t1.index(2,3,20))
"""

# mcq : 
"""
t1=(12,13,14,0,[1,2,3],89,90)

t1[4].append("krishiv")
print(t1)

options : 
a. error  #s m m p 
b. (12,13,14,0,[1,2,3,"krishiv"],89,90)  #p d  b  p d  j 
c. (12,13,14,0,[1,2,3],"krishiv",89,90)  # c 
d. none  # m 
"""

# task 1 :  add in tuple last position.
"""
input  : t1=(12,2,3,4,5,67.89,99,77,44,22,11,67.89,2)
output  : t1=(12,2,3,4,5,67.89,99,77,44,22,11,67.89,2,"krishiv")
""" 







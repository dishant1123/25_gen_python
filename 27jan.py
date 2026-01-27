# modules : random  , math  , cmath , datetime , calender , timedelta   

import random as r 

"""a= r.random()  # 0-1 value float  ==> 1  excluded 
a=r.randrange(1,10,2)  # start  stop step  ==> 10 excluded
a=r.randint(1,10)  # start  stop step  ==>both  point included

print(a)
"""

"""
result =r.choice([1,2,3,4,"moksh","het"])
result =r.choices([1,2,3,4,"moksh","het"],k=3)
print(result)
"""

"""a=[1,2,3,4,5,6,7,8,9,10]
# print(a)
r.shuffle(a)
print(a)
"""

import math as m 

"""print(m.sqrt(29))
print(m.factorial(6))
print(m.pow(3,4))
print(m.e)
print(m.pi)
print(m.fsum([1,2,3,4,5,5,666,7]))
print(m.floor(45.89))  # only int value print 
print(m.ceil(45.01))  # round up value 

print(m.exp(1))  # e rise of power of  x    e value is  : 2.71 
print(m.remainder(10,3))
print(m.gcd(20,10))
print(m.lcm(40,35))

"""

# rock paper scissor  :
"""
1. user  vs  comp 
2. [rock ,paper ,scissor]  : function  : choice  ==> 
3. score display   ===> 10   loop  10 times 

logic :
    1. if u ==rock  and comp ==rock  or 
    2. case : u==rock and comp == scissor or u ==scissor and comp ==paper  or u ==paper and comp ==rock    ===> userscore  += 1
    3. else  ==> comscore +=1
    
result  : 
    userscore  = 7  comscore  = 3
    so user win the game . 
"""
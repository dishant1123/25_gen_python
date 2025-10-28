# loop  : 
"""
syntax  : 

for variable name  in range(start , stop  , step) : 
    print(variable name)
"""

# 1-100 : 

"""
for i in range(1,100):
    print(i,end=" ")
"""

# 100-1 : 

"""for i in range(100,0,-1):  # start =100 , stop  = 1 step  =-1 
    print(i,end=" ")
"""

"""for i in range(1,100,3):
    print(i,end=" ")
"""

# prime  , perfect , amg , twin , strong , reverse , pelindrome : 

# perfect number  : 
"""
6 factors  : 1,2,3,6 
sum = 1+2+3 =6 

28  factors  : 1,2,4,7,14,28 
sum = 1+2+4+7+14 =28

100 factors  : 1,2,4,5,10,20,25,50,100 
sum = 1+2+4+5+10+20+25+50 = 100  not  perfect number   

"""
"""
n=int(input("enter the  number : "))
sum =0 
for i in range(1,n):  # 1,5  ==> 6
    if n % i==0 :
        sum =sum +i 
if sum ==n :
    print("perfect number")
     
"""

# amg :  
"""
153 : 3 digit 

each digit  : 1**1  5**3  3**3   = 1 125 27 
sum = 1+125 +27 =153  ==>amg 

1634 : 4 digit 
each  digit  : 1*1*1*1  6*6*6*6  3*3*3*3   4*4*4*4 
               1       1296       81       256      
sum = 1634 amg 

"""

# buit in function  : len  min max sorted sum 

# s=1234567891567
# s2 =str(s)  # "123456"
# print(type(s2))

# print(len(str(s)))

"""n=int(input("enter the  number  : "))#153 
sum =0 
digits =len(str(n))
temp =n        
for i in range(digits) : # 2 ,3 
    r= n %10           # r =  1 % 10 =1  
    sum =sum +pow(r,digits)  # sum = 153
    n = n //10     # n = 0

if sum ==temp :
    print("amg")
"""

# twin number : 
"""
123  twin  number : 

each digit sum = 1+2+3 =6 
each mul = 1*2*3 =6 

sum ==mul  ==> twin 
"""

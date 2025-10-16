# loop  : 
"""
1. for 
2. while 
3. while true 

break  contunie  pass 
"""
# syntax : 
"""
for  variable name in range(start ,stop,step):
    print(variable name)
"""

# 1-100 : 
"""
for i in range(1,101):
    print(i,end=" ") 
"""
# 100-1 : 
"""for x in range(100,0,-1):  # start 100 , stop 0 ,step -1
    print(x,end=" ")
"""
# odd :
"""
for v in range(1,101,2):
    print(v,end=" ")
"""

# even : 
"""for v in range(0,101,2):
    print(v,end=" ")

"""
#-90 to  45 print    45 to  -90 print 

"""n=int(input("enter the num : "))
for i in range(1,n+1):
    print(i,end=" ")
"""

"""start = int(input("enter the start : "))
stop= int(input("enter the stop : "))

for i in range(start, stop+1):
    print(i,end=" ")
"""

# prime  : 
"""n=int(input("enter the num : "))
count =0 

for i in range(1,n+1):
    if n % i==0 :
        count +=1 
if count ==2 :
    print(n,"is a prime number")
"""
#amg : 

# built in function  :  len min max sorted sum 
"""
n=int(input("enter the  number : "))  # 1634 
digit =len(str(n))  # 4 
sum=0 
temp= n 
for i in range(digit):  # 3-4 
    r = temp %10     # r =1 %10=1 
    sum =  sum + pow(r,digit)  # sum =1634
    temp  = temp //10   # temp = 0

if sum == n :
    print("amg")
"""

# strong : 
"""
145 : each digit factorial : 1! =1  5! =120  4! =24 
sum = 1+120 +24 =145 

"""

# while  : 
"""i=1 
while i <=100 :
    print(i,end=" ")
    i+=1
"""
# nested  loop  : 
"""
start =int(input("enter the start : "))
stop =int(input("enter the stop : "))

for i in range(start,stop+1):  # 23 -200
    digits = len(str(i))
    temp =i 
    sum =0 
    for j in range(digits):
        r= temp %10
        sum = sum + pow(r,digits)
        temp = temp //10
    if sum ==i :
        print(i,end=" ")
"""

# pattern  : 
""" 
1.         2.         3.          4.          5.           6. 
* * * * *  *          * * * * *   1            5 4 3 2 1   1 2 3 4 5
* * * * *  * *        * * * *     1 2          5 4 3 2     2 3 4 5 
* * * * *  * * *      * * *       1 2 3        5 4 3       3 4 5
* * * * *  * * * *    * *         1 2 3 4      5 4         4 5
* * * * *  * * * * *  *           1 2 3 4 5    5           5 

"""
# 1 : 
"""
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
"""
#2 :
"""
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
"""
# 3 :
for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

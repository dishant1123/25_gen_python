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
n=int(input("enter the num : "))
count =0 

for i in range(1,n+1):
    if n % i==0 :
        count +=1 
if count ==2 :
    print(n,"is a prime number")
        
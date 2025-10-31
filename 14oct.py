# loop :  
"""
1. for  loop :  entry  control  loop 
2. while  loop :  entry , exit control loop
3. while  True : exit loop   

# break , continue , pass :  
"""

# for loop  syntax : 
"""
c /cpp:

for(start; con ; inc/dec)
{
    printf();
} 
python  : 

for (variable name) in range(start , stop , step):
    print(variable name)
"""

# 1-100 : 

"""
for i in range(1,101):
    print(i,end=" ")
"""

# 100 -1 : 

"""
for x in range(100,0,-1):  # step 
    print(x,end=" ")
"""
# odd : 
"""for  h in range(1,101,2):  # start  1  stop 101  step  2 
    print(h,end=" ")
"""

# even : 

"""
for a in range(2,100,2):
    print(a,end=" ")
"""
"""
for g in range(100,0,-2):
    print(g,end=" ")
"""

# user input  : 

"""n=int(input("enter  the  number  :"))

for i in range(1,n+1):
    print(i,end=" ")
"""

# 2 user input  :

"""
start =int(input("enter  the  start  :"))
stop =int(input("enter  the  stop  :"))

for x  in range(start,stop,-1):
    print(x,end=" ")
"""

# prime , perfect , amg , twin , strong , reverse , pelindrome :

# prime  : 

"""n=int(input("enter  the  number  :"))
count =0 
for i in range(1,n+1):
    if n % i ==0: 
        count +=1
if count ==2 : 
    print("prime")
"""    
# perfect number  : 
"""
perfect : 

6 factors : 1,2,3,6  
sum = 1+2+3 = 6 

28 factors  : 1,2,4,7,14,28 
sum = 1+2+4+7+14 =28 perfect 

"""

start=int(input("enter the number  start : "))
end = int(input("enter the number end  : "))

for i in range(start ,end+1): 
    count = 0 
    for j in range(1,i+1 ): 
        if i % j ==0 : 
            count +=1 
    if count ==2 :
        print(i,end=" ")
# conditoinal statement : 
"""
if con : 
    print()
else : 
    print()
    
ladder : 

if con :
    print()
elif con :
    print()
else :
    print()
"""

#loop  : 

"""
1. for  
2. while  
3. while true
"""

"""
syntax : 

for  (variable name) in range(start , stop ,step ):
    print() 

while  : 

i= intial value  
while  con :
    print()
    i+=1 assignemnt operator  : a= a+b  a+=b , i =i+1  i+=1
    
while true : 

i= intial value  
while True :
    print()
    if con : 
        break 
"""

# break  : 
"""
for i in range(10):
    if i==5:
        break
    print(i)
print(i)
"""

# contunie  : 
"""
for i in range(10):
    if i==5:
        continue
    print(i)
print(i)
"""

# pass : 
"""for i in range(10):
    if i==5:
        pass 
    print(i)
print(i)
"""

# 1-100 : 

"""i=1 
while True :
    print(i,end="    ")
    i+=1
    if i==100 :
        break
"""

# match : 

a=int(input("enter the  number  1:"))
b=int(input("enter the  number 2 :" ))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6.floor division")

choice=int(input("enter the choice :"))

match  choice :
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3 :
        print(a*b)
    case 4 :
        print(a/b)
    case 5 :
        print(a%b)
    case 6 :
        print(a//b)
    case _:
        print("invalid choice")
# task 1 : exit con 
# task  :2 7 press ==> enter the new number  


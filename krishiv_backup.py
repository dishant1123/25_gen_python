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

"""a=int(input("enter the  number  1:"))
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

"""

# list  : mutable sequnece of element .    ==> you can change the list

"""
l1=[1,2,3,4,5,"krishiv",True,8j,67.89]

print(l1)
print(type(l1))
"""
# list element access though index : 

"""
l1=[1,2,3,4,5,"krishiv",True,8j,67.89]

print(l1[4])

l1[2]= "modi"  # update the  list  though index
print(l1)
"""

# built in function  :  len min max sorted sum reversed

"""
l1=[10,2,3,4,5,67.89,90]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to desc 
print(sum(l1))
print(sorted(l1,reverse=True))  #  desc to asc 

"""
# method  : 

l1=[10,2,3,4,5,67.89,90,10]

# l1.append(100)
# print(l1)

# l1.clear()
# print(l1)

# l2=l1.copy()
# print(l2)

# l1.insert(3,450)
# print(l1)

# print(l1.count(10))

# print(l1.index(10))
# print(l1.index(10,1,20))

# pop , remove : 

# l1.pop()  # if not give any arg then remove  the  last element. 
# print(l1)

# l1.pop(3)# arg : index 
# print(l1)

# l1.remove(10)
# print(l1)

# l1.sort()
# print(l1)

# l1.sort(reverse=True)
# print(l1)

# l1.reverse()
# print(l1)

# l2=["apple","mango","banana","orange","kiwi"]
# l1.extend(l2)
# print(l1)


# slicing  :

"""l1=[10,2,3,4,5,67.89,90,10]

print(l1[4])
print(l1[2:5])
print(l1[ :7])
print(l1[1 :])
print(l1[-2])
print(l1[-2 :4])
print(l1[-2 :-4 :-2])
print(l1[-4 :-2])
print(l1[ : : 2])
print(l1[ : : -1])
"""
"""
ask : 3 take list from user append all element in list and remove duplicate element in the list.
         input : [1,2,3,4,4,5,5,6,7,8,9,9,10]
         output : [1,2,3,4,5,6,7,8,9,10]
"""

"""n=int(input("enter the  number  of element  in the list : "))
l1=[]
for i in range(n):
    ele=int(input("enter the element : "))
    l1.append(ele)
print(l1)  # [1 2 2 3 3 4 5]
l2=[]
for i in l1 :
    if i not in l2 : 
        l2.append(i)
print(l2)
"""

# task :2 peli : 

"""n=int(input("enter the  number  of element  in the list : "))
l1=[]
for i in range(n):
    ele=int(input("enter the element : "))
    l1.append(ele)
print(l1)  # [121 123 222 453 131]
l2=[]"""
"""for i in l1 : 
    rev =0 
    temp =i 
    while temp >0 :
        r= temp%10
        rev = rev *10 +r 
        temp = temp //10  
    if rev ==i :
        l2 .append(i)
print(l2)   

"""
"""l2=[]
for i in l1:
    if str(i) == str(i)[ : : -1]:
        l2.append(i)
print(l2)

"""

# tuple  : immutable squence  of element .
  
"""t1=(1,2,3,4,5,"krishiv",True,8j,67.89)
print(t1)
print(type(t1))

t2= 1,2,3,4,5,6,7,8
print(t2)
print(type(t2))

t3=("")
print(t3)
print(type(t3))

t4=""
print(t4)
print(type(t4))
"""

# built in function  :  len  min max sorted sum 

"""
t1=(12,2,3,4,5,67.89)

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc 
print(sum(t1))
print(sorted(t1,reverse=True))  #  desc to asc
"""

# slicing  : 

# t1=(12,2,3,4,5,67.89)

"""t1[4] ="krishiv"  # not possible  bcz  tuple is  immutable 
print(t1)
"""
"""print(t1[4])
print(t1[ :5])
print(t1[ 1:])
print(t1[-1])
print(t1[ : : -1])
"""

# method  : 

"""
t1=(12,2,3,4,5,67.89,12,45,78)

print(t1.count(12))
print(t1.index(12))
print(t1.index(12,1,20))

"""

# mcq : 
"""
t1=(12,13,14,0,[1,2,3],89,90)
#   0   1  2 3   4     5   6 

t1[4].append("krishiv")
print(t1)

options : 

a. error 
b. (12,13,14,0,[1,2,3,"krishiv"],89,90)
c. (12,13,14,0,[1,2,3],"krishiv",89,90)
d. none

"""

# task :1 add one element in tuple  last position.
"""
input  : t1=(12,2,3,4,5,67.89,12,45,78)
output  : t1=(12,2,3,4,5,67.89,12,45,78,"krishiv")
"""

"""t1=(12,2,3,4,5,67.89,12,45,78)
print(list(t1))
"""
# task  :2 changes  in  last elemet in tuple. 

"""
input : t1= [(1,2,3),(4,5,6),(7,8,9)]
outut  : t1= [(1,2,100),(4,5,100),(7,8,100)]
"""

# dict : mutable   ==> key value pair 

"""
d1={"phy":90 ,"che" :78}
print(d1)
print(type(d1)) 

d2= {90 :89 ,"com":100}
print(d2)
print(type(d2))

"""

# update  : 
"""
d1={"phy":90 ,"che" :78}
d1["com"] =100
print(d1)
"""
# built in function  : len  min max sorted sum 

"""
d1={"phy":90 ,"che" :78}
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  # asc to desc 
print(sorted(d1,reverse=True))  # asc to desc 
"""

# slicing  :
"""
d1={"phy":90 ,"che" :78}
print(d1[0]) # slicing not poss in dict 
"""

# method : 
d1={"phy":90 ,"che" :78}

"""d1.clear()
print(d1)
"""
"""d2=d1.copy()
print(d2)
"""
"""print(d1.keys())
print(d1.values())
print(d1.items())
"""

# print(d1.get("phy"))

"""l1=["krishiv","het"] 
# d1={"krishiv":90 ,"het" :90}

d2 =dict.fromkeys(l1,90)
print(d2)
"""
# d2["het"] =88
# print(d2)

"""d1.update(d2)
print(d1)
"""

d1={"phy":90 ,"che" :78,"com":900}

"""print(d1.pop("phy"))
print(d1)
"""
"""
d1.popitem() # remove last value  from dict
print(d1)
"""

d1.setdefault("ss",89)
print(d1)
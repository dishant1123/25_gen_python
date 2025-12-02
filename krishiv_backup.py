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

"""d1.setdefault("ss",89)
print(d1)
"""

# string : immutable sequence of character .

"""
s1 = "my name is krishiv."
print(s1)
print(type(s1))

"""
# built in function  : len min max sorted  

"""
s1 = "my name is krishiv."
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to desc
print(sorted(s1,reverse=True))  # desc to asc
"""

# slicing: 

"""
s1 = "my name is krishiv."

print(s1[3])
print(s1[2])
print(s1[2 :5])
print(s1[2 :8 :2])
print(s1[-2])
print(s1[ : :-2])
print(s1[ : :2])
print(s1[ : :-1])
"""

# task :1 
"""
input : dishant dipakkumar shah 
output : d.d.shah
"""

# task :2 
"""
ask user to enter the two string  and  swap the first three character of the second string with the first three character of the first string.

input  1: color 
input  2 :full 

ouput 1:fulor 
output 2:coll
"""
# method  : 

s1 ="my Name is krishiv."

"""print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.swapcase())
print(s1.casefold())
"""

"""s2="happy chirstmas" 
print(s2)
print(s2.center(50,"@"))
print(s2.ljust(50,"@"))
print(s2.rjust(50,"@"))
"""
# count ,  index , rindex, find rfind : 
s1 ="my Name is krishiv."

"""print(s1.count("k"))
print(s1.count("i"))
print(s1.count("i",9,20))

print(s1.index("k"))
print(s1.index("i"))
print(s1.index("i",9,20))
print(s1.index("i",14,20))

print(s1.rindex("i"))
print(s1.rindex("i",9,15))
print(s1.rindex("i",8,12))

print(s1.find("k"))
print(s1.find("i"))
print(s1.find("i",9,20))
print(s1.find("i",14,20))


print(s1.rfind("i"))
print(s1.rfind("i",9,15))
print(s1.rfind("i",8,12))
"""

# task  :3 
"""
input  :  i am going to goa next month. 
ouptut :  first o index : 6 
         second o index : 12 
         third o index :  15
         fourth o index : 24 
         
"""

# replace : 

"""s1 ="my Name is krishiv."

print(s1.replace("k","K"))
print(s1.replace(" ","",1))
print(s1.replace("is","",2))
"""

# task :4 
"""
input  : restart 
output : resta#t
"""

# task  :5 
"""
ask user to enter the  string  and  replace the first space  and last space with "#" and "_" respectively.

input  :my name is krishiv.
output  my_name is_krishiv. 
"""
s2="my name is krishiv modi."

"""modify_string = s2.replace(" ","_",1)[: : -1].replace(" ","_",1)[: : -1]
print(modify_string)
"""

"""s2 = input("Enter a string: ")

modify_string = ""

# find first and last space positions
first_space = s2.find(" ")
last_space = s2.rfind(" ")

i = 0
while i < len(s2):
    ch = s2[i]

    if i == first_space:
        modify_string += "_"
    elif i == last_space and i != first_space:
        modify_string += "_"
    else:
        modify_string += ch

    i += 1

print(modify_string)
"""

# join  : 

"""l1=["my","name","is","krishiv"]
# join  with space : my name is  krishiv. 
s2 ="@".join(l1)
print(s2)
"""
s1="my name is  krishiv."

"""print(s1.split()) 
print(s1.split("i"))
print(s1.split("is"))

print(s1.rsplit("z"))
print(s1.rsplit("is"))
"""
# partition , rpartition : 

"""s1="my name is  krishiv."
print(s1.partition(" "))
print(s1.partition("i"))
print(s1.rpartition("i"))
"""

# strip , lstrip , rstrip :

"""s3="          happy chirstmas        "

print(s3)
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())
"""
s1="my name is  krishiv."

"""print(s1.startswith("my "))
print(s1.startswith("my n"))
print(s1.startswith("y n"))
print(s1.endswith("."))
print(s1.endswith("krishiv."))
print(s1.endswith("  krishiv."))
"""

# isalpha,isdigit,isnumreic,isalnum : 

s3 ="krishiv"
# print(s3.isalpha())

s4="krishiv90"
# print(s4.isalnum())

# isdigit , isnumeric ,isdecimal :

"""s5="1234"
print(s5.isdigit())

s6="123.46"
print(s6.isnumeric())
print(s6.isdecimal())

"""
"""s1 = "12345"
print(f"'{s1}':")
print(f"  isdecimal(): {s1.isdecimal()}")  # True
print(f"  isdigit():   {s1.isdigit()}")    # True
print(f"  isnumeric(): {s1.isnumeric()}")  # True

"""
"""s2 = "\u00B2"  # Superscript two
print(f"'{s2}':")
print(f"  isdecimal(): {s2.isdecimal()}")  # False (not a strict decimal)
print(f"  isdigit():   {s2.isdigit()}")    # True (considered a digit)
print(f"  isnumeric(): {s2.isnumeric()}")  # True (considered numeric)
"""
"""s3 = "\u2153"  # Vulgar fraction one third
print(f"'{s3}':")
print(f"  isdecimal(): {s3.isdecimal()}")  # False
print(f"  isdigit():   {s3.isdigit()}")    # False
print(f"  isnumeric(): {s3.isnumeric()}")  # True (considered numeric)
"""

# task  :1 
"""
ask user to enter the  valid  password below conditions . 

1. len  min 8 character. 
2. must contain  at least one  upper case character.
3. must contain  at least one special character.
4. must contain  at least one digit.
"""
"""while True:
    password =  input('enter a password :')
    a = False
    b = False

    if len(password)<8:
        print('Invalid Password...')
    else:
        for i in password:
            if i.isdigit():
                a = True
            elif not i.isalnum():
                b = True
            if a and b:
                print('Valid Password...')
                break
        else:
            if not a :
                print('Minimum 1 digit Required...')
            if not b:
                print('Minimum 1 Special Character Required...')
    if a and b :
        break
"""

# set : mutable  but  no repeation  allowed in set. unordered collection of unique elements.

"""
s1={1,2,3,4,5,5,6,7,7,8,9,10} 
print(s1)

l1=[1,2,2,3,3,4,4,5,6,7,7,8,9]
l2 =set(l1)
print(list(l2)) 
"""

# built in function  :  len  min max sorted sum

"""s1={1,2,3,4,5,5,6,7,7,8,9,10} 

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to desc 
print(sorted(s1,reverse=True))  #  desc to asc
print(sum(s1))
"""

# slicing  : 
"""
s1={-1,0,3,4,5,5,6,7,7,8,9,10}
print(s1[1])  # not slincing  poss in  set bcz of unordered collection.

"""

# method  : 

# s1={-1,0,3,4,5,5,6,7,7,8,9,10}

"""s1.add(120)
print(s1)
"""

"""s1.clear()
print(s1)
"""
"""s2= s1.copy()
print("s2=",s2)
"""

"""s1={1,2,3,4}
s2={2,4,6,8,10}
s3={1,2,3,4,5,6,7,8,9,10}
"""
"""print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

print(s1.symmetric_difference(s2))
"""
"""print(s1.difference(s2))
s1.difference_update(s2)
print(s1)
"""
"""print(s1.symmetric_difference(s2))
print(s1)

s1.symmetric_difference_update(s2)
print(s1)
"""

"""print(s1.intersection(s2))
print(s1)
s1.intersection_update(s2)
print(s1)
"""

# isdisjoint , issubset , issuperset ,: 

"""
s1={1,2,3,4}
s2={1,3}
s3={1,2,3,4,5,6,7,8,9,10}
"""
# print(s1.isdisjoint(s2))
# print(s3.issuperset(s2))

# print(s2.issubset(s1))

s1={1,2,3,4}

"""s1.remove(2)
print(s1)

s1.discard(63)
print(s1)
"""
"""
s2={"krishiv","het"}

s2.update(s1)
print(s2)
"""
"""s1={0,1,2,3,4}
s1.pop(4)

print(s1)
"""

# frozen set : immutable  set 

"""fz =frozenset({1,2,3,4,5,6,6})
print(fz)
print(type(fz))

"""

# function  : 

"""
type  : 

1. no arg no return 
2. no arg  with return
3. with arg no return
4. with arg  with return
"""
# 1 :no arg no return
"""def a():  # def keyword   a() ==> func name 
    c=12 
    d=90   # func intialization 
    print(c+d)
a() # func calling  
a()

"""

# 2  with arg no return

"""def g(a,b):
    print(a+b)
a=int(input("enter a :"))
b=int(input("enter b :"))
g(a,b)
"""
# 3 : no arg  with return 

"""def h():
    a=int(input("enter a :"))
    b=int(input("enter b :"))
    c=a+b 
    return c 
print(h())
"""

# 4 : with arg  with return

"""def t(a,b):
    return a+b 

print(t(12,45))
"""

# *args : it takes only numreric arg. 

"""def gh(*args):
    print(sum(args))

gh(12,12,3,5,6,7,8,9,0,34)
"""

"""def hj(*x):
    sum =0 
    for i in x : 
        sum =sum + i 
    return sum 
print(hj(12,3,4,5,6,7,8,334,56))
"""

# **kwargs : it takes key value pair arg.

"""def k(**kwargs):
    for i ,j in  kwargs.items():
        print(f"{i} : {j}")
k(name="krishiv",age=21,city="delhi")
"""

# employees manag system : 
"""
1. add
2. delete
3. update
4. search
5.display
"""

"""d1={}

def add():
    id =int(input("enter the  emp id :"))
    name =input("enter the  emp name :")
    salary =int(input("enter the  emp salary :"))
    d1[id] =[name,salary]
    print("emp added successfully")
    
def delete_emp():
    del_id =int(input("enter the  emp id :"))
    if del_id in d1: 
        del d1[del_id]
        print("emp deleted successfully")
    else :
        print("emp not found")

def update_emp():
    update_id =int(input("enter the  emp id :"))
    if update_id in d1:
        name =input("enter the updated emp name :")
        salary =int(input("enter the updated emp salary :"))
        d1[update_id]=[name,salary]
        print("emp updated successfully")
    else :
        print("emp not found")
"""      
# def serach_emp():
    
# def display_emp():
    
# add()
# add()
# print(d1)
# delete_emp()
# print(d1)
# update_emp()
# print(d1)

"""
menu  : 
1. add
2. delete
3. update
4. search
5.display   choice = 
"""
# local variable :

"""
within function declare local variable  . 
"""

"""
def x ():
    a=100   #local variable 
    print(a)
x()
print(a)  # local variable  not accessible outside function
"""

# global variable :
"""
x=100 
def g():
    print(x)  # global 
g()
print(x)  # global can be accessed outside function
"""

# modify global variable :

"""x=100 
def g():
    global x 
    x=200 
    print(x)
g()
print(x)
"""
# lambda : one line  function 
"""
syntax : 

lambda arg : expression 
"""

"""def add(a,b):
    return a+b
print(add(12,45)) 
"""
"""a= lambda x,y : x+y 
print(a(23,56))
"""
# built in function  :  len  min max sorted sum

"""b =lambda x : sorted(x,reverse=True)
print(b([10,2,3,4,5,6,7]))
"""
# print : 
"""
a=lambda x : print("hello",x)
a("krishiv")
"""
# conditional statement :

"""def big():
    a=int(input())
    b=int(input())
    if a>b :
        print("a is greater than b")
    else :
        print("b is greater than a")
big()
"""
"""
x= lambda a,b : print("a is  big") if a>b else print("b is big")
x(121,56)
"""

# list sort :
# below list sort by second  element. 
l1=[[1,2],[0,1],[4,-5]]


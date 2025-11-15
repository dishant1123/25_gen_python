"""
print("hello  prince")
print('live  in ahmedabad.')
print("study in INDUS Clg.")
print("work in  HP.")
"""
# comment : 
"""
1. single  line comment : # 
2. multi  line  comment : """ """ or '''  '''
"""

# data type  :
"""
1. int  : pos or  neg values==> no  limit 
2. float : decimal value 
3. char/string : store name , a to z , special character
4. bool :  True or False
5. complex number : 2 part ==> real  part and imaginary part  ex : 23 +6j  23 ==> real part , 6j ==> imaginary part
"""

"""a=20
print(a)
print("a=",a)
print(type(a))  # type casting

b=12345678123456782345678912345678923456789123456789456789
print(b)
print("b=",b)
print(type(b))  # type casting

c= 12.45 
print(c)
print("c=",c)
print(type(c))  # type casting

d=1234562345.1234123434534534534545456
print(d)
print("d=",d)
print(type(d))  # type casting

e="prince patel"
print(e)
print("e=",e)
print(type(e))  # type casting

f=True
print(f)
print("f=",f)
print(type(f))  # type casting

g=23 +8j
# 23 real part, 8j ==> imaginary part
print(g)
print("g=",g)
print(type(g))  # type casting
h=45+9j 
print(g+h)
"""

# operator : 
"""
1. airthmetic : + - * / % //
2. comparison : == != > < >= <=
3. logic : and or not
4. membership : in ,  not in
5. assignment : = += -= *= /= %= //=
"""

"""a=10
b=3 
print(a/b)  # div
print(a//b)  # floor div 
print(a%b)  # reminder 

l1=[1,2,3,4,5]

print(10 in l1)
print(10 not in l1)
"""

# user  input  string :

"""a=str(input("enter  the name  :"))
b=input("enter  the sur-name  :")
print(a)
print(b)
print(a,b)
print(a+b)
"""
# user  input  number :

"""a=int(input("enter  the  number 1:"))
b=int(input("enter  the  number 2:"))
print(a)
print(b)
print(a+b)  # you can't store decimal value in int type
"""

"""a=float(input("enter  the  number 1:"))
b=float(input("enter  the  number 2:"))
print(a)
print(b)
print(a+b)  

"""

# task  : 1 
"""
ask user to enter the  two  number  (int type ) and concate them.

input  a:10 
input  b:20
output :1020
"""

# match  : 

"""a=int(input("enter the  number 1 : "))
b=int(input("enter the  number 1 : "))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulo")
print("6.floor  division")
choice =int(input("enter the  choice :"))

match  choice :
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print(a%b)
    case 6:
        print(a//b)
"""

# factorial  : user ==> 5 ==>120 


# pattern  : 

""" 
1.          2.            3.        4.           5.           6.
* * * * *   *          * * * * *    1            5 4 3 2 1    1 2 3 4 5
* * * * *   * *        * * * *      1 2          5 4 3 2      2 3 4 5
* * * * *   * * *      * * *        1 2 3        5 4 3        3 4 5
* * * * *   * * * *    * *          1 2 3 4      5 4          4 5
* * * * *   * * * * *  *            1 2 3 4 5    5            5
"""

# 1: 
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()        
"""
#2 : 
"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()        
"""

# 3: 
"""
for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end=" ")
    print()        
"""

"""
5:          6 : 
a           e d c b a 
a b         e d c b 
a b c       e d c
a b c d     e d
a b c d e   e

"""
# ord : ==> character  ascci value  print  
"""ch='a'
for i in range(1,6):   # 1 
    for j in range(1,i+1):   # 1 , 2 
        print(chr(ord(ch)+j-1),end=" ")    # 
    print()
"""


#1. string  2 list  3 tuple 4 dict  5 set 
"""
# #list : mutable  sequence element  ==> you can changes in list. 

# """
# l1=[1,2,3,4,56,7,8,9,"jay",9j,90.89]
# print(l1)
# print(type(l1))
 
# """
# # list element access though  index : 
# """
# l1=[1,2,3,4,56,7,8,9,"jay",9j,90.89]

# print(l1[0])
# l1[2] ="viral"
# print(l1)
# """
# # slicing  : 

# """
# l1=[100,2,3,4,56,7,8,9,90,91,90]
# # pos index : l to  r  ==> 0 
# # neg index : r to l  ==>-1 

# print(l1[4])
# print(l1[2:4])
# print(l1[2:4])
# print(l1[ :8])
# print(l1[1 : ])
# print(l1[-1])
# print(l1[-5 : -1])
# print(l1[5 : -1])
# print(l1[-5 : 1])
# #       -5 -4-3-2-1 0 1 2 3 4 5

# print(l1[2: 8 :2])
# print(l1[1: 8 :3])
# print(l1[ :   :2])
# print(l1[ :   :-2])
# print(l1[ :   :-1])

# """

# # built in function  : len min max sorted sum 
# """
# l1=[100,2,3,4,56,7,8,9,90,91,90]
# print(len(l1))
# print(min(l1))
# print(max(l1))
# print(sorted(l1))   # asc to desc
# print(sorted(l1,reverse=True))
# print(sum(l1))
# """

# # method  : 
# l1=[100,2,3,4,56,7,8,9,90,91,90]

# """
# l1.append(2000)  # add element in last 
# print(l1)

# l2= l1.copy()
# print("l2=",l2)

# """
# """
# l1.clear()
# print(l1)
# """

# """
# l2=["apple","banana","cherry"]

# l1.extend(l2)
# print(l1)
# """

# # index : 
# """
# l1=[100,2,3,4,56,7,8,9,90,91,90,56]

# print(l1.index(56))
# print(l1.index(56,5,20))

# """

# l1=[100,2,3,4,56,7,8,9,90,91,90,56]

# # remove  , pop : 
# # l1.pop(4)  # arg  ==> index 
# # print(l1)

# """
# l1.remove(8)
# print(l1)
# """
# # l1.sort()
# # print(l1)

# """
# l1.reverse()
# print(l1)
# """

# print(l1.count(56))
# """

# data type  : list , tuple , dict, set, string 

#list : mutable sequence element ==> you can changes in list.

"""
l1=[1,2,3,4,56,7,8,9,"jay",9j,90.89]

print(l1)
print(type(l1))

"""

# list element access though  index :

"""
l1=[1,2,3,4,56,7,8,9,"jay",9j,90.89]
print(l1[0])
l1[3] ="prince"  # update element  ==>though index 
print(l1)
"""

# built in function  : len  min max sorted sum 

"""
list1=[1,2,3,4,56,7,8,9,56,9,90.89]

print(len(list1))
print(min(list1))
print(max(list1))
print(sorted(list1))  # asc to desc
print(sorted(list1,reverse=True)) # desc to asc 
print(sum(list1))
"""

# slicing : 
"""l1=[1,2,3,4,56,7,8,9,56,9,90.89]
# pos index : l to  r  ==> 0 
# neg index : r to l  ==>-1

print(l1[4])
print(l1[2 :5])   # start 2  end 5  ==>ending index is not included
print(l1[: 6])
print(l1[1: ])
print(l1[-2])

print(l1[2 :8:2]) # start 2  end 8 ==>step 2
print(l1[1 :8: 3]) # start 1  end 8 ==>step 3

print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])
"""

# method  : 

# l1=[1,2,3,4,56,7,8,9,56,9,90]

# l1.append(2000) 
# print(l1)

# l1.insert(2,234)
# print(l1)

# l1.clear()
# print(l1)

# l2 =l1.copy()
# print(l2)

# print(l1.count(56))

# l1=[1,2,3,4,56,7,8,9,56,9,90]

# print(l1.index(56))
# print(l1.index(56,5,20))

"""
l2=["apple","banana","cherry"]
l1.extend(l2)
print(l1)
"""

# delete  :  pop () , remove()

"""
l1.pop(5)  # arg :index
print(l1)

l1.remove(56)
print(l1)
"""

"""l1.sort()
print(l1)
"""

"""l1.reverse()
print(l1)
"""

# task :1 

"""n=int(input("enter the  number :"))
l2=[]
for i in range(1,n+1):
    element =int(input("enter the  number :"))
    l2.append(element)
print(l2)  # [1,2,3,4,5]
even=0
odd=0
for i in l2 :
    if i % 2==0:
        even=even+i 
    else :
        odd=odd+i
print(even)
print(odd)
"""
# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
# names2[0] = 'Alice'
# names3[1] = 'Bob'
# print(names1)
# print(names2)
# print(names3)
# names1 = ["alice", "bob", "charlton", "daman"]
# names2 = ["alice", "bear", "charlton", "daman"]
# names3 = ["alice", "bob", "charlton", "daman"]
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10
# print(sum)


"""l2=[1,1,2,3,4,5,6,7,8,1,1]

print(l2.count(1))
print(l2.index(1))
print(l2.index(1,3,20))
"""

"""x = [1, 2, 3]
# y = "vyom"
# x.extend(y)
print(x)

x.remove(3)
print(x)

x.sort(reverse=True)
print(x)
"""
# adv list  : 

l1=[[1,2,3],[4,5,6],[7,8,9]]
     #0       1       2
"""print(l1)
for i in l1 :
    print(i)
"""
"""
1 2 3 
4 5 6
7 8 9
"""
"""print(l1[0])
print(l1[2])

print(l1[0][1])
print(l1[0 :2][0:1])
print(l1[ : :-1])
"""

l2=[[1,10],[4,6],[0,9]]

# sort the array element for 2 postion element : 

# output  : [[4,6],[0,9],[1,10]]

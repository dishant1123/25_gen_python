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

a=int(input("enter the  number 1 : "))
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
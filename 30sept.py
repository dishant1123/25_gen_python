# print("hello moksh.")
"""
print('live  in ahmedabad.')
print("study in INDUS Clg.")
print("work in  HP.")
"""
# comment  : 
"""
1. single line comment : # 
2. multi  line  comment : """ """ or '''  ''' 
"""

# escape sequence  character : 
"""
1. \n : new line
2. \t : tab 
3. \b : backspace
4. end= : remove the white  space after the end of the word.
"""
# moksh patel
"""print("moksh",end="\b\b")
print("patel")
"""
# variable declaration rule:
"""
1. not start with :  special character, number 
2. valid  : _ 
"""

# data type  : 
"""
1. int : pos or neg value    ==> no limit 
2. float : decimal value 
3. char/ string  : store name , a to z , special character 
4. bool :  True or False 
5. complex number: 2 part ==> real  part and imaginary part  
"""

"""a=10 
print(a)
print("a=",a)
print(type(a))  # type casting 
 
b =12345678123456782345678912345678923456789123456789456789 
print(b)
print("b=",b)
print(type(b))  # type casting 

c =12.45 
print(c)
print("c=",c)
print(type(c))  # type casting

d =1234562345.1234123434534534534545456
print(d)
print("d=",d)
print(type(d))  # type casting

e='@#$%^&'
print(e)
print("e=",e)
print(type(e))  # type casting

f =True
print(f)
print("f=",f)
print(type(f))  # type casting

g=23+9j
# 23 real part, 9j ==> imaginary part
print(g)
print("g=",g)
print(type(g))  # type casting
j=45 +12j

print(j+g)
"""

# c:\new_folder\bin\python.exe 
"""
print("c:\\new_folder\\bin\python.exe ")
"""

# user input string :

"""a=str(input("enter  the name  :"))
b=input("enter  the sur-name  :")
print(a)
print(b)
print(a,b)  # comma create space in python.  
"""

# user input  number  : 

"""
a=int(input("enter  the  number 1:"))
b=int(input("enter  the  number 2:"))
print(a)
print(b)
"""
"""a=float(input("enter  the  number 1:"))
b=float(input("enter  the  number 2:"))
print(a)
print(b)
"""
#task :1 
"""
ask user to enter the  two  number  (int type ) and concate them. 

input a=10 
input b =20
output :1020
"""
"""
a=int(input("enter  the  number 1:"))
b=int(input("enter  the  number 2:"))
print(a,end="")
print(b)
"""

# opearator  : 

"""
1. airthematic : + - * / % //
2.comparison : == != > < >= <=
3.logic : and or not
4.membership : in ,  not in 
5.assignment : = += -= *= /= %= //=
"""

a=20 
b=201
# print(a/b)# division
# print(a//b)   # only int  
# print(a%b)

# print(a!=b)
# a=a+b 
# a+=b
# print(a)

"""
a=20
b=201

"""
# print(a>b and a!=b)
# print(a>b or a!=b)

"""
l1=[1,2,3,4,90]

print(1 in l1)
print(10 not in l1)
"""

# match  : 
a=int(input("enter  the  number 1:"))
b=int(input("enter  the  number 2:"))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulo")
print("6.floor  division")
choice=int(input("enter  the  operation  :"))

match choice :
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

# menu  hotel  :
"""
1. panjabi  : qty  , price ==> total  bill 
2. south indian 
3. maxican 
"""

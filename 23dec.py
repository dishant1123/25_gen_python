# string  : immutable sequence of characters

"""
s1="my name is ram."
print(s1)
print(type(s1))
"""

# built in function  : len min max sorted sum 
"""s1="my name is ram."

print(len(s1))
print(min(s1)) # ascci value 
print(max(s1))
print(sorted(s1))
print(sorted(s1,reverse=True))
"""
# concatenate two string :

"""a="pinal"
b="patel"
print(a+b)
"""

# slicing  : 

"""
s1="my name is pinal patel and live in ahmedabad."
#index start  with  : 0   ==> l to r 
#neg index start  with  : -1 ==> r to l 

print(s1[2])
print(s1[3:9])
print(s1[-2])
print(s1[-5 : -1])
print(s1[-1 : -5])  #      -5-4-3-2-1  0
print(s1[-1 : -5 : -1])  #
print(s1[2: 7 :2])
print(s1[:  :2])
print(s1[:  :-2])
print(s1[:  :-1])
"""

# task  :1 
"""
input  : "dishant dipakkuamr shah"
output  : d.d.shah
"""
# task  :2 
"""
ask user to enter the two string and  swap the first three character of the second string and wise versa.

input  a : color 
input  b : full 

output a: fulor 
output b: coll  
"""
# method  : 

s1="My name Is pinal patel and live in ahmedabad."

"""
print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.casefold())
print(s1.swapcase())
"""
s2="happy holi"

"""
print(s2.center(50))
print(s2.center(50,"-"))
print(s2.ljust(50,"-"))
print(s2.rjust(50,"-"))
"""

s1="My name is pinal patel and live in ahmedabad."

"""
print(s1.count("i"))
print(s1.count("i",9,20))  # 9 start pos index 20 end pos index
"""

"""
print(s1.replace("pinal","heli"))
print(s1.replace("is",""))
print(s1.replace(" ",""))
print(s1.replace(" ","",1))
print(s1.replace(" ","",2))
"""

# task  :3 
"""
input  a : "restart"
output a: resta@t  
 """
 
# task  :4 

"""
ask user to enter the  string  and  first space and  last space  replace with "_" . 

input a:"My name is pinal patel and live in ahmedabad."
output a :"My_name is pinal patel and live in_ahmedabad."
"""

s="My name is pinal patel and live in ahmedabad."

modify_string =s.replace(" ","_",1)[: : -1].replace(" ","_",1)[: : -1]
# print(modify_string) 

s1="my name is ram and wife name is sita."
print(s1.replace(" ","_"))
print(s1.replace(" ","_",2))
print(s1.replace(" ","_",4))
print(s1.replace("is"," ",1))



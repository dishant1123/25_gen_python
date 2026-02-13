# 4 pillar : 
"""
1. inheritance 
    a. single b.multiple c.multi level  d.hirechy  e.hybrid 
2. polymorphism
    a . method overriding  b. method overloading
3. encapsulation  
    a. set  method  b. get method
4. abstraction  
"""

# constructor : 
"""
1. automatically called when  object is  created. 
2. no return type 

types : 
1. default constructor
2. parameterized constructor
3. non-parameterized constructor
4. constructor overloading
5. copy constructor
"""

# default constructor : 

"""class student  :
    def __init__(self):  # def  ==> function  __init__ ==> special method,constructor 
        print("my name is het.")
        print("default constructor called")

s=student()
"""

# non-parameterized constructor :

"""class vehicle : 
    def __init__(self):
        self.__model = "toyota"
        self.__color = "white"
        self.__production_year = 2000 
        print("non-parameterized constructor called")
    
    def show(self):
        print("model : ",self.__model)
        print("color : ",self.__color)
        print("production year : ",self.__production_year)
        
v=vehicle()
# print(v.color)
# print(v.model)
# print(v.production_year)
v.show()
"""

# parameterized constructor :

"""class vehicle :
    def __init__(self,name,model,color):
        self.name =name 
        self.model =model
        self.color =color
        print("parameterized constructor called")
        
v=vehicle("toyota","prius","white")
print(v.name)
print(v.model)
print(v.color)

"""
# constructor  overloading :

"""class student : 
    def __init__(self):
        print("default  constructor called")
        
    def __init__(self):
        self.name ="het"
        self.age =19 
        print("non parameterized constructor called")
    
    def __init__(self,name,age):
        self.name =name
        self.age =age
        print("parameterized constructor called")
    
    def show(self):
        print("name : ",self.name)
        print("age : ",self.age)
# s=student()
s1=student("moksh",20)
# s2=student()
s1.show()
"""
# shallow copy :
"""
l1=[1,34,56,78,90]

l2=l1 
l2.append(100) 

print(l1)
print(l2)
"""
# deep copy : 
"""l1=[1,34,56,78,90]

l2=l1.copy()
l2.append(900)

print(l1)
print(l2)
"""

import copy 

class student : 
    def __init__(self,name,marks):
        self.name =name
        self.marks =marks
        
s1= student("het",99)

# shallow copy :
s2=copy.copy(s1)

# deep copy :
s3 =copy.deepcopy(s1)

print(s2.name)
print(s3.name)
        
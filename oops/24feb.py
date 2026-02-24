# encapsulation  : 
"""
encapsulation  means binding data(variables)  and methods(functions) together inside a class and restricting access to them to some of the object's components . 

private  and protected   ==>access , modify  

"""

# ex :1 

"""class student : 
    def __init__(self):
        self.__name ="moksh"
        self.__age =20
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
s=student()
print("name is  : ",s.get_name())
print("age is  : ",s.get_age())
s.__name ="pinal"  # not  modify  or udpdate  bcz of  private  . 
s.__age =19
print("name is  : ",s.get_name())
print("age is  : ",s.get_age())
"""

# ex :2 set method  : 

"""class student : 
    def __init__(self):
        self.__name ="pinal"
        self.__age =20 
        
    def set_name(self,new_name):
        self.__name =new_name 
        
    def set_age(self,new_age):
        if new_age >18:
            self.__age =new_age
        else :
            print("age should be greater than 18")
            
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
s=student()
print("before using  set method  : ")
print("name is  : ",s.get_name())
print("age is  : ",s.get_age())

print("using  set method  : ")
s.set_name("moksh")
s.set_age(21)
print("name is  : ",s.get_name())
print("age is  : ",s.get_age())
"""



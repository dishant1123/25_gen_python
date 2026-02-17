"""
inheritance : to inherit properties and methods from a parent class

1. single inheritance
2. multiple inheritance
3. multi level inheritance
4. hirearchy
5. hybrid 
"""

# 1 single  inheritance : 

"""
class student : 
    # def __init__(self):
    #     self.name = "pinal" 
    #     self.age =19 
    name = "pinal"
    age =19
class teacher (student): 
    def __init__(self):
        # super().__init__()  # base class constructor
        # student.__init__(self)
        self.t_name ="dr vyas"
    def show(self):
        print("student information ")
        print("student name  is  : ",self.name)
        print("student  age is  : ",self.age)
        print("teacher information")
        print("teacher name is  : ",self.t_name)

t=teacher()
t.show()
t.name ="moksh"
t.age =20 
t.show() 
"""

# ex :2 

"""class student : 
    def __init__(self,name,age):
        self.__name =name   # name  age  is  private 
        self.__age =age
    def display(self):
        print("name is  : ",self.__name)
        print("age is  : ",self.__age)
class teacher (student):
    def __init__(self, name, age,p_name):
        super().__init__(name, age)
        self.p_name =p_name
        
    def show(self):
        print("student information ")
        self.display()
        print("teacher information")
        print("teacher name is  : ",self.p_name)
        
t=teacher("moksh",20,"dr vyas")
t.show()
"""

# ex :3 

"""class student : 
    def __init__(self,name,age):
        self._name =name   # name  age  protected 
        self._age =age
        
class teacher (student):
    def __init__(self, name, age,p_name):
        student.__init__(self,name,age)
        self.p_name =p_name
    def show(self):
        print("student information ")
        print("student name  is  : ",self._name)
        print("student  age is  : ",self._age)
        print("teacher information")
        print("teacher name is  : ",self.p_name)
        
t=teacher("moksh",20,"dr vyas")
# t.show()
t._name = "pinal"
t._age = 19
t.show()
"""

#  2. multiple inheritance   vs   multi level 
"""
class a :                           class a :
class b :                           class b (a):
class c (a,b)                       class c (b):
"""


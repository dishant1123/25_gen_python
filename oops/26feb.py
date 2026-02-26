# destructor :  destructor is a function that is called when an object is destroyed
"""
__del__ is a special method that is called when an object is destroyed
"""

# ex :1 

"""class student : 
    def __init__(self,name):
        self.name =name
        print("constrcutor called")
    
    def __del__(self):
        print("destructor called")
        
s1=student("john")
# del s1 # destructor is called
"""    

# ex :2 

"""class parent :
    def __init__(self,name):
        self.name=name
        print("constrcutor called")
        print("name is  : ",self.name)
        
    def __del__(self):
        print("destructor called")

class child(parent):
    def __init__(self, name,age):
        super().__init__(name)  # calling parent constructor
        self.age =age 
        print("constrcutor called child")
        print("age is  : ",self.age)
    
    def __del__(self):
        print("destructor called child")
        super().__del__()
        
# object : 
c=child("john",20)
del c 
"""

# polymorphism :  many  forms 
"""
1. method  overloading : compile time  
2. method overriding  : run time
"""

# method  overloading  : 
"""
same method  ==> diff parameters

in python  method  overloading  not support like traditonal way for  c++. 
"""
# ex :1 

"""class calculator : 
    def add(self,b,a=10,c=90):
        return a+b+c 
    
obj =calculator()
print(obj.add(10,20,30))
print(obj.add(10))
"""    

# ex : 2 using  *args

"""class Sum : 
    def add(self,*args):
        return sum(args)

s=Sum()
print(s.add(10,20,30))
print(s.add(10))
print(s.add(10,20))
"""

# method  overriding  : 

"""class animal : 
    def sound(self):
        print("animal sound")

class cat(animal):
    def sound(self):
        print("cat sound")

class dog(animal):
    def sound(self):
        print("dog sound")
        
c=cat()
c.sound()

d=dog()
d.sound()
"""
# constructor  : 

"""class parent : 
    def __init__(self):
        print("parent  class constructor called ")
        
class child(parent):
    def __init__(self):
        super().__init__()
        print("child class constructor called ")
        
c=child()
"""

# both  : method  overriding  and  method overriding 

class bank : 
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print("bank constructor called")
        
    def deposit(self,amt,bonus=0):  # loading with default value 
        self.balance+=amt+bonus
        print("deposit amt  : ",amt)
        if bonus >0:
            print("bonus is : ",bonus)
        print("after  deposit  + bonus amt your balance is : ",self.balance)
        
    def calculate_interest(self):
        interest =self.balance * 0.04 
        print("interest is 4% : ",interest)
        
class savings(bank):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        print("savings constructor called")
    
    def calculate_interest(self): # method  overriding
        interest =self.balance * 0.08
        print("interest is 8% : ",interest)
        
print("normal bank")
ac1 = bank("moksh",25000)
ac1.deposit(6000)
ac1.deposit(1000,500)
ac1.calculate_interest() 

print("savings bank")
ac2=savings("het",55000)
ac2.deposit(30000)
ac2.calculate_interest()
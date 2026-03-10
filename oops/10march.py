"""
abtraction  : means  hiding internal implementations detalis and showing only essential features to the user. 

1. abstract class : from abc import ABC  ==> abc ==> abstract base class 
2. abstract method : @abstractmethod ==> abstract method

"""
# ex :1 

from abc import  ABC,abstractmethod 
"""
class animal(ABC):
    
    @abstractmethod
    def sound(self): 
        pass 
    
class dog(animal):
    def sound(self):
        print("bhowww bhowww")
        
class cat(animal):
    def sound(self):
        print("meowwww mewoooww")
        
class bird(animal):
    def sound(self):
        print("tweet tweet")
        
d=dog()
c=cat()
b=bird()

d.sound()
c.sound()
b.sound()
"""

# ex :2 
"""
class bank_account(ABC):
    def __init__(self,name):
        self.name=name
        self.__balance=0 
        
    @abstractmethod
    def deposit(self,amount):
        pass 
       
    @abstractmethod
    def withdraw(self,amount):
        pass 
    
    @abstractmethod
    def get_balance(self):
        pass 

    def display(self): 
        print(f"name:{self.name} balance:{self.__balance}")
        
class savings_account(bank_account):
    def __init__(self, name):
        super().__init__(name)
        self.accnumber =123456356
        self.__balance=0
        
    def deposit(self, amount):
        self.__balance+=amount
        print(f"deposited {amount} to {self.name}")
        
    def withdraw(self, amount):
        self.__balance-=amount
        print(f"withdraw {amount} from {self.name}")
        
    def get_balance(self):
        return self.__balance
    
a=savings_account("pinal")
a.display()
print("your initial balance is  : ",a.get_balance())
a.deposit(25000)
a.withdraw(13000)
print("your final balance is  : ",a.get_balance()"""

# ex :3 real  life example  : 
"""
class bank(ABC): 
    def __init__(self,name,balance):
        self.name =name      
        self.__balance =balance  # private variable
        self._bank = "SBI"      # protected variable
    
    def show_customer(self):
        print(f"customer name is {self.name}")
        print("bank name is ",self._bank)
        
    def _show_balance(self): 
        print(f"balance is {self.__balance}")
    
    @abstractmethod 
    def acconut_type(self):
        pass 

class savings_account(bank):
    def __init__(self, name, balance,interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        
    def acconut_type(self):
        print("savings account")
    
    def show_details(self):
        self.show_customer()
        self._show_balance()
        print(f"interest rate is {self.interest_rate}")
        
s=savings_account("pinal",100000,5)
s.show_details()
"""

# class method  : cls  ==>   

# static  method  : 

class student : 
    school ="Ahmedabad international school"
    
    def __init__(self,name,marks):
        self.name =name
        self.marks =marks
        
    @classmethod
    def change_school(cls,new_name):
        cls.school =new_name
        
    @staticmethod
    def is_pass(marks):
        if marks >=40:
            return "pass" 
        else :
            return "fail"
        
s =student("pinal",90)
s1=student("adil",30)

# using static method : 
print(s.name,student.is_pass(s.marks))
print(s1.name,student.is_pass(s1.marks))
    
student.change_school("Tulip international school")
print(s.school)
print(s1.school)

# next class : magic / special method  ex : __str__ , __add__ ,__len__ 
        


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
print("your final balance is  : ",a.get_balance())
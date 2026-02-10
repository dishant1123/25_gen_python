# protected : 

"""class student : 
    _name ="het"  # name age  salary  ==> protected  data members
    _age =20 
    _salary =90000 
    
class teacher (student):
     def show(self):
         print("name : ",self._name)
         print("age : ",self._age)
         print("salary : ",self._salary)
         
t=teacher()
t.show()
"""

# ex : oop with bank  

class bank : 
    bank_account =1234567890
    ac_holder_name ="moksh"
    balance =50000 
    
    def deposit(self,amt):
        self.balance +=amt
        print("deposited : ",amt) 
    
    def withdraw(self,amt):
        if self.balance -amt >=10000 :
            self.balance -=amt
            print("withdraw : ",amt) 
        else :
            print("min balance  10000 rs.")
    def show_balance(self):
        print("balance : ",self.balance)

    def info(self):
        print("BANK ACCOUNT INFORMATION")
        print("Bank Account Number : ",self.bank_account)
        print("Account Holder Name : ",self.ac_holder_name)
        print("Current Balance : ",self.balance)
b=bank()
b.info()
b.deposit(10000)
b.withdraw(25000)
b.show_balance()

"""
task  :1  generate  pin when user deposit  and withdraw money  then  enter  pin  and also verify the pin if  user enter  wrong  pin then user can't  withdraw or  deposit  money. 
"""
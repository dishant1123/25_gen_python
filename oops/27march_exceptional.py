"""
excepational handling  :  to  handle  error .

ex : 1 
a=10 
b=0 
print(a/b)  ==> zero division error  ==> msg  ==> you can't divide by zero

syntax : 

try : 
    risky code
execpt :
    run if  error  occurs 

"""
# ex :1 

"""try : 
    a=int(input("enter a number "))
    b=int(input("enter another number "))
    result =a/b
    print(result)
except :  # zero division error
    print("you can't divide by zero")
"""

# ex :2 specific exception handling : 

"""try : 
    a=int(input("enter a number "))
    b= 10/a 
except ZeroDivisionError :
    print("you can't divide by zero")
except ValueError :
    print("invalid input")
"""

# ex :3 using  else : 

"""try : 
    a=int(input("enter a number "))
    y=10/a 
    
except ZeroDivisionError :
    print("you can't divide by zero")
else : 
    print(y)
"""

# ex : 4 using  finally 

"""try : 
    a=10/0 
except ZeroDivisionError :
    print("you can't divide by zero")
finally:
    print("this will always run")
"""    
# ex :5 file handling : 

"""try : 
    file = open("moksh.txt",'r')
    context = file.read()
    print(context)
except FileNotFoundError :
    print("file not found")
finally : 
    print("closing file....")
    try : 
        file.close()
    except : 
        pass 
"""

# ex :6 custom exception :

"""class negative_number(Exception):
    pass 

try : 
    a=int(input("enter a number "))
    if a <0 :
        raise negative_number("negative number  not allowed")
except negative_number as n :
    print(n)
"""

# ex :7 bank system (oop + file + exception)

class bankaccount: 
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
        
    def deposit(self,amount):
        try : 
            if amount<=0:
                raise ValueError("amount should be positive")
            self.balance+=amount
            return f"deposited {amount} to account {self.accno}"
        except ValueError as e:
            print(e)
            
    def withdraw(self,amount):
        try : 
            if self.balance -amount <=10000:
                raise ValueError("insufficient funds")
            self.balance-=amount
            return f"withdrawn {amount} from account {self.accno}"
        except ValueError as e:
            print(e)
    
    def display(self):
        return f"account name : {self.name} \n account number : {self.accno} \n balance : {self.balance}"
    
try : 
    name =input("enter the name ac holder : ")
    acc_no=int(input("enter the account number : "))
    balance =int(input("enter the initial balance : "))
    
    b =bankaccount(name,acc_no,balance)
    
    d= int(input("enter the deposit amount : "))
    dep_result = b.deposit(d)
    
    w= int(input("enter the withdraw amount : "))
    with_result = b.withdraw(w)
    
    info= b.display()
    
    file = open("SBI_BANK.txt","w")
    file.write("=========BANK TRANSACTIONS DETAILS=========\n")
    file.write(info + "\n")
    file.write(dep_result + "\n")
    file.write(with_result + "\n")
    file.close()
    
    print("data saved to SBI_BANK.txt")
    
except ValueError as e:
    print("error occured enter valid input")

except FileExistsError :
    print("file already exists")
    
finally : 
    print("closing file....")
    
"""
task :1 
                        HDFC BANK 
DATE : 27-03-2023                              ACCOUNT_HOLDER_NAME :PINAL PATEL                         
BRANCH : AHEMEDABAD                            ACCOUNT_TYPE : SAVINGS
                                               ACCOUNT_NUMBER : 789000124523
                                               
SRNO          TRANSACTION_DATE        AMOUNT    DR       CR         BALANCE
1             27-03-2023              20000             20000       20000 
2             27-03-2023              30000             30000       50000 
3             27-03-2023                      38000                 12000 

"""
# next  : numpy 
# function  ; 
"""
employees management  system  : 

1. emp add
2. emp delete 
3. emp update
4. emp search
5. emp display
6 .exit  
"""

"""
d1= {"name" : "moksh" , "age" : 20 , "gender" : "male"}
d1["sports"] ="cricket"
print(d1)
"""
'''d1={}
def emp_add():
    id=int(input("enter the id : "))
    name =input("enter the  name  : ")
    age=int(input("enter the age : "))
    salary=int(input("enter the salary : "))
    d1[id] =[name,age,salary] 
    print("emp added successfully")

def update_emp():
    update_id=int(input("enter the  id you want  to  update :")) # 1  
    if update_id in d1 :
        name =input("enter the  new name  : ")
        salary =int(input("enter the  new salary  : "))
        age=int(input("enter the  new age  : "))
        d1[update_id]=[name,salary,age]
        print("emp updated successfully")
    else :
        print("emp not found")

def delete_emp():
    delete_id =int(input("enter the  id you want  to  delete :"))
    if delete_id in d1 :
        del d1[delete_id]
        print("emp deleted successfully")
    else :
        print("emp not found")
        
def emp_serach(): 
    search_id=int(input("enter the  id you want  to  search :"))
    if search_id in d1 :
        print(d1[search_id])
    else :
        print("emp not found")
        
def display_emp():
    

def main():
    

emp_add()
emp_add()
print(d1)

update_emp()
print(d1)

# delete_emp()
# print(d1)

emp_serach()
print(d1)
"""
id   name    age  salary  
1     het    20     90000
2     moksh  21     89000 
"""
'''
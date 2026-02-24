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
# encapsulation  + inheritance  : 

class employee : 
    def __init__(self,name,id,salary):
        self.__id =id
        self.__name =name
        self.__salary =salary
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary
    
    def set_name(self,new_name):
        self.__name =new_name
        
    def set_salary(self,new_salary):
        self.__salary =new_salary
        
    def display(self):
        print("employee id is  : ",self.__id)
        print("employee name is  : ",self.__name)
        print("employee salary is  : ",self.__salary)
        
class manager(employee): # single 
    def __init__(self, name, id, salary,department):
        super().__int__(name, id, salary)  
        self.__department =department
        
    def get_department(self):
        return self.__department
    
    def set_department(self,new_department):
        self.__department =new_department
        
    def display_manager(self):
        self.display()
        print("manager department is  : ",self.__department)
        
class developer(employee):   # hirechy 
    def __init__(self, name, id, salary,languages):
        super().__int__(name, id, salary)
        self.__languages =languages
    
    def get_languages(self):
        return self.__languages

    def set_languages(self,new_languages):
        self.__languages =new_languages
        
    def display_developer(self):
        self.display()
        print("developer languages is  : ",self.__languages)
        

class senoir_developer(developer):# multi level 
    def __init__(self, name, id, salary,languages,experience):
        super().__init__(name,id,salary,languages)
        self.__experience =experience
    
    def get_experience(self):
        return self.__experience

    def set_experience(self,new_experience):
        self.__experience =new_experience
        
    def display_senoir_developer(self):
        self.display_developer()
        print("senoir developer experience is  : ",self.__experience)
class bonus : 
    def __init__(self,bonus):
        self.__bonus =bonus
    
    def get_bonus(self):
        return self.__bonus
    
class tech_lead(developer,bonus) : # multiple 
    def __init__(self, name, id, salary,languages,bonus):
        developer.__init__(self,name,id,salary,languages)
        bonus.__init__(self,bonus)
    
    def display_tech_lead(self):
        self.display_developer()
        print("tech lead bonus is  : ",self.__bonus)
        
class hybridemp(senoir_developer,bonus):  # hybrid
    def __init__(self, name, id, salary, languages, experience,bonus):
        senoir_developer.__init__(self,name, id, salary, languages, experience)
        bonus.__init__(self,bonus)
    
    def display_hybridemp(self):
        self.display_senoir_developer()
        print("bonus : ",self.__bonus)
        
# menu driven  : 

employee_list=[] 

def add_employee():
    emp_id =int(input("enter employee id : "))
    emp_name =input("enter employee name : ")
    emp_salary =int(input("enter employee salary : "))
    emp =employee(emp_name,emp_id,emp_salary)
    employee_list.append(emp)
    print("employee added")
    
    
def display_employee():
    if not employee_list:
        print("no employee added")
    else :
        for emp in employee_list:
            emp.display()
        
def main():
    while True :
        print("1.add employee")
        print("2.display employee")
        print("3.exit")
        choice =int(input("enter choice : "))
        if choice ==1:
            add_employee()
        elif choice ==2:
            display_employee()
        elif choice ==3:
            break 
        else :
            print("invalid choice")
main()

# home  : delete  , update   : 
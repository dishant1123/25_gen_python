# oops : 
"""
class  : blueprint  of  object

object : instance  of class . 

 fruits  : 
      mango , chiku , banana , apple 
      
que  : 1 class multiple  objects   ==> yes 
que  : 2 multiple  class  object 1  ==> no 

==========================================================================

type  : 
1. public : accessible from anywhere
2. private : with  the class only 
3. protected : with  the class and sub class (inheritance)

"""

# ex :1 
"""class student :   # student  class  ==> name 
    name = "pinal"   # name age  clg  ==> class data members
    age =20 
    clg = "LJ(old)"
    
s=student()  # s object  ==> student 
print("name : ",s.name)
print("age : ",s.age)
print("clg : ",s.clg)
"""

# ex :2  function  

"""class student :   # student  class  ==> name 
    name = "pinal"   # name age  clg  ==> class data members
    age =20 
    clg = "LJ(old)"

    def show(self):  #self  ==> keyword  ==> current  object  ==> data member , method  ==> access 
        print("name : ",self.name)
        print("age : ",self.age)
        print("clg : ",self.clg)
    
s=student()  # s object  ==> student 
s.show()
s.name ="moksh"
s.age =18 
s.clg="Indus"
s.show()
"""

# ex :3 private 

"""class student : 
    __name ="priyanshi"  # __name ,__city  ==> private  data members
    __city = "rajkot"
    
    def show(self):
        print("name : ",self.__name)
        print("city : ",self.__city)

s=student() 
# print(s.__name)  # not  accessible bcz of  private .  
# print(s.__city)
s.show()
s.__name ="moksh"  # not  update  bcz  of  private .
s.__city="delhi"
s.show()
"""
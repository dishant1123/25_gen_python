# hirearchy :  multiple  derived class  inherit  same base class. 
"""
class a 
class b (a) 
class c (a) 
class d (a)
"""

"""class vehicle : 
    def __init__(self):
        self.name = "vehicle"
        self.type ="two wheeler or four wheeler"
    
    def show(self):
        print("vehicle name is  : ",self.name)
        print("vehicle type is  : ",self.type)

class car (vehicle):
    def __init__(self,model):
        super().__init__()  # based class constructor
        self.model =model
    
    def display(self):
        self.show()
        print("car model is  : ",self.model)
        
class bike(vehicle):
    def __init__(self,speed):
        super().__init__()
        self.speed =speed

    def display(self):
        vehicle.show(self)
        print("bike speed is  : ",self.speed)
        
c=car("audi-Q7")
c.display()

b=bike(220)
b.display()
"""

# hybrid : multiple + multi level  combination . combination  of  one or more than one inheritance. 
"""
class a 
class b(a)
class c(a) 
class d(b,c)
"""
class vehicle : 
    def __init__(self):
        self.name = "vehicle"
        self.type ="two wheeler or four wheeler"
    
    def show(self):
        print("vehicle name is  : ",self.name)
        print("vehicle type is  : ",self.type)
class car (vehicle):
    def __init__(self,model,**kwargs):
        super().__init__(**kwargs)  # based class constructor
        self.model =model
        
    def display(self):
        self.show()
        print("car model is  : ",self.model)
        
class bike(vehicle):
    def __init__(self,speed,**kwargs):
        super().__init__(**kwargs)
        self.speed =speed
        
    def display(self):
        self.show()
        print("bike speed is  : ",self.speed)

class truck(car,bike):
    def __init__(self,capacity,model,speed):
        super().__init__(model=model,speed=speed)
        self.capacity =capacity
        
    def info(self):
        car.display(self)
        bike.display(self)
        print("truck capacity is  : ",self.capacity)
        
t=truck(12000,"audi-Q7",220)
t.info()

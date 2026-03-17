"""
special method  : __str__ , __add__ ,__len__

"""
# ex :1  __str__ ==> used to how define an  object should be printed

"""class student : 
        def __init__(self,name,marks):
            self.name =name 
            self.marks =marks
        def __str__(self): 
            return f"name:{self.name} marks:{self.marks}"
        
s=student("pinal",90)
print(s)"""

                
# ex :2 __add__  ==> used to add two objects

"""class number : 
    def __init__(self,value):
        self.value =value
        
    def __add__(self,other):
        return number(self.value+other.value)
    
    def __str__(self):
        return f"value:{self.value}"
    
n1 =number(10)
n2 =number(20)
n3 =n1+n2
print(n3)
"""

# ex :3 __len__  ==> used to define the length of an object

"""class mylist : 
    def __init__(self,values):
        self.values =values
        
    def __len__(self):
        return len(self.values)
    
obj = mylist([1,2,3,4,5])
print(len(obj))
"""

# ex :4 combine : 
"""
class book : 
    def __init__(self,pages):
        self.pages =pages
    
    def __str__(self):
        return f"book with pages:{self.pages}"
    
    def __add__(self,other):
        return book(self.pages+other.pages)
    
    def __len__(self):
        return self.pages

b1 =book(100)
b2 =book(200)

b3 =    b1+b2
print(b1)
print(b3)
print(len(b1))"""


# file handling :
"""
1.read mode   : only exiting file  
2.write mode  : new file create + write  ==> exiting  file + overwrite 
3.append mode : new file create + write  ==> exiting  file + last add

with  open  ==> open  , fopen()
f.close() ==> file  close 
f.read() ==> read file
"""

# write  mode  : 

"""
with  open("moksh.txt","w")  as f : 
    f.write("hey  moksh  ....... how are you ????\n")
    f.write("i am fine.\n")
    f.write("sir can i leave  meeting  bcz  of i going to somewhere ??\n")
    f.write("no  .. sry\n")
    f.close()
"""

# write mode : exiting  file  
"""with  open("moksh.txt","w")  as f : 
    f.write("hey  vyom  ....... how are you ????\n")
    f.write("i am fine.\n")
    f.write("old LJ clg . bcz vyom  love clg culture.\n")
    f.close()
"""

# read mode : 

"""with open("moksh.txt","r") as f :
    # result =f.read()  # all file content read 
    # result =f.readline()  # only one line read
    result =f.readlines()  # all lines read
    print(result)
"""

# append mode :
"""
with open("moksh.txt","a") as f :
    f.write("clg name is  indus. \n")
    f.write("best friend name is  vyom.\n")
    f.close()
"""



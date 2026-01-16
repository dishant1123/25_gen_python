# lambda function  : 
"""
one  line  function  . 

syntax : lambda args : expression 
"""

# ex : 1 

"""
def add(x,y):
    return x+y 
print(add(1,67))
"""
"""x= lambda a,b :a+b
print(x(23,56))
"""
# ex 2 :  len min max sorted  

"""a=lambda x :sorted(x) 
print(a((1,2,30,4,7,5)))
"""

# ex :3 using conditional statements
"""
def big(a,b):
    if a>b :
        print("a is bigger")
    else :
        print("b is bigger")
big(10,20)
"""
"""
x =lambda a,b : print("a is  big")if a>b else print("b is big")
x(90,3) 
b= lambda a,b,c : max(a,b,c)
print(b(10,20,30))
"""

# task  :1 sort by second element. (using def function ) 
"""
input  : a= [[1,2],[0,4],[5,-2]]
output  : a= [[5,-2],[1,2],[0,4]]
"""
"""
[1,2]  ==> index 0   ==> 1,2  ==> 1 index num  0  2 index num 1
[0,4]  ==> index 1  ==>  0,4  ==> 0 index num  0  4 index num 1
[5,-2] ==> index 2  ==> 5,-2  ==> 5 index num  0  -2 index num 1
"""
# print(a)
# print("always  sorted first value : ",sorted(a))

"""def second_value(a) :
    return a[1]   #  index 1 

a= [[1,2],[0,4],[5,-2]]
result = sorted(a,key=second_value)
print(result)
"""
a= [[1,2],[0,4],[5,-2]]
x = sorted(a,key =lambda x :x [0])
print(x)


"""
1. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

2. Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

"""


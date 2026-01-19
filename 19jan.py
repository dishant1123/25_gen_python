#filter :
"""
jan  to dec  fin trasactions  ==> june  
==> not  given a new list  using filter  . it is  only  provided information  which  you want . 
"""

"""
l1= [1,2,3,4,5,6,7,8,9,10]
odd=[] 
even =[] 
for i in  l1 : 
    if i % 2==0 : 
        even.append(i)
    else :
        odd.append(i)
print(odd)
print(even)  
"""
"""l1= [1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda x  :x % 2==0 ,l1))
b=tuple(filter(lambda x  :x % 2==1 ,l1))

print("even list  : ",a)
print("odd list  : ",b)
"""

# map  : it gives a new list . 

"""
l1=[1,5,2,6,8,4]
l2=[] 
for i in l1: 
    l2.append(i *5)
print(l2)
"""

"""l1=[1,5,2,6,8,4]
a=list(map(lambda x  :x*5 ,l1))
print("list  element  multiplied  by 5 : ",a)
"""

"""
4. Write a Python program to remove all elements from a given list present in another list using lambda.

Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]

5. Write a Python program to reverse strings in a given list of string values using lambda.

Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


6. 
Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
"""
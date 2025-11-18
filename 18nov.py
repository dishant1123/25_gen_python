"""
input  : l1=[10,20,30,40,50,60,70,999,99,45,50] 
ouptut : print  second  largest number in the list  ===> 99 
"""

"""l1=[10,20,30,40,50,60,70,999,99,45,50]
l1.sort()
print("l1=",l1)
print("second largest number in the list  ===> ",l1[-2])
"""

# task  :2 
"""
take list from user append all element in list and print pelindorme num in list 
 
input : [121 , 131 , 123 ,145 , 789 ]
output :  [121,131]

"""

"""n=int(input("enter number of elements in list : "))
l1=[] 

for i in range(n): # 0-4
    ele = int(input("enter element : "))
    l1.append(ele)
print(l1) # [121 , 131 , 123 ,145 , 789 ]
l2=[]
for i in  l1 :  #121 
    if str(i) == str(i)[ : : -1] :   # "121"  == "121"  
        l2.append(i)
print(l2)
"""
# str  list  tuple  dict  set 


"""n=int(input("enter number of elements in list : "))
l1=[] 
for i in range(n): # 0-4
    ele = int(input("enter element : "))
    l1.append(ele)
print(l1) # [1,2,3,3,4,4,5,5,6,6,7,9,1,10 ]

l2=[] 
for i in l1 :   # 1
    if i not in l2:   # if 1 not in l2 
        l2.append(i)  # l2 = [1,2,3]
print(l2) 
"""

"""
hw : 
1.
Write a Python program to find a list of integers with exactly two occurrences of nineteen
	 and at least three occurrences of five.  count 
	Return True otherwise False.
	Input:
	[19, 19, 15, 5, 3, 5, 5, 2]
	Output:
	True
	Input:
	[19, 15, 15, 5, 3, 3, 5, 2]
	Output:
	False
	Input:
	[19, 19, 5, 5, 5, 5, 5]
	Output:
	True
 
2. 
Write a Python program that accepts a list of integers and calculates the length and the 
	fifth element. Return true if the 
	length of the list is 8 and the fifth element occurs thrice in the said list.
	Input:
	[19, 19, 15, 5, 5, 5, 1, 2]
	Output:
	True
	Input:
	[19, 15, 5, 7, 5, 5, 2]
	Output:
	False

"""
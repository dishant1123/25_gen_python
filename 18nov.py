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

n=int(input("enter number of elements in list : "))
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
        
# str  list  tuple  dict  set 

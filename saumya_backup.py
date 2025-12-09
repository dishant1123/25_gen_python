# list  : mutable sequence of data , ==> changes in list . 

"""
l1=[1,2,3,4,5,"krishiv",True,8j,67.89]
print(l1)
print(type(l1))
"""
# built in function  :  len min max sorted sum reversed

"""
l1=[1,2,3,4,5,45,12,8,67,89]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to desc
print(sorted(l1,reverse=True))  # desc to asc
print(sum(l1))
"""

# slicing  : 
"""
index start  : 0 ,1,2,3,4 .....  l to r 
neg index : -1 ,-2   ==> r to l
"""

l1=[10,20,30,40,50,45,12,8,67,89]

"""
l1[3]="saumya" # update in list 
print(l1)
"""
"""print(l1[2])
print(l1[2:5])  #start index 2 end index 5
print(l1[ : 6])
print(l1[1 : ])
print(l1[1 :7:2 ])
print(l1[ : : 2])
print(l1[-2])
print(l1[ : : -2])
print(l1[ : : -1])
"""

# method :  

l1=[10,20,30,40,50,45,12,8,67,89,10]

# l1.append(200)
# print(l1)

# l2=l1.copy()
# print("l2=",l2)

# l1.clear()
# print(l1)

# l2=["apple","mango","banana","orange","kiwi"]
# l1.extend(l2)
# print(l1)

# print(l1.count(10))

# print(l1.index(10))
# print(l1.index(10,1,20))

# l1.insert(4,567)
# print(l1)

# pop , remove : 
"""l1.pop()  # if not give any arg then remove  the  last element.
print(l1)

l1.pop(3)# arg : index
print(l1)
"""

# l1.remove(12)
# print(l1)

# l1.sort()
# print(l1)

# l1.sort(reverse=True)
# print(l1)

# l1.reverse()
# print(l1)

# tuple  : immutable sequence of data . ==> can't change the tuple .

"""
t1=(1,2,3,4,5,"krishiv",True,8j,67.89)
print(t1)
print(type(t1))

t2= 1,2,3,4,5,6,7,8
print(t2)
print(type(t2))

t3=90 ,
print(t3)
print(type(t3))
"""

# built in function  :  len  min max sorted sum

t1=(100,2,3,4,5,8,67.89)
"""print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc
print(sorted(t1,reverse=True))  # desc to asc
print(sum(t1))


t1[2] ="samuya"
print(t1)  # error : bcz of immutable tuple
"""

# method : 

"""
t1=(100,2,3,4,100,8,67.89)

print(t1.count(100))
print(t1.index(100))
print(t1.index(100,1,9))
"""

# task : 1 take list from user append all element in list and print odd and even element sum .
n=int(input("enter the  number  of element  in the list : "))
l1=[] 

for i in range(n):
    ele =int(input("enter the element : "))
    l1.append(ele)
print(l1)  # [1,2,3,4,5]

oddsum =0 
evensum =0
for i in l1 : 
    if i %2==0 :
        evensum +=i
    else :
        oddsum +=i
print(oddsum)
print(evensum)

"""
task : 3 take list from user append all element in list and remove duplicate element in the list.
         input : [1,2,3,4,4,5,5,6,7,8,9,9,10]
         output : [1,2,3,4,5,6,7,8,9,10] 
"""
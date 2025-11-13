# python  : 
"""
data type  : 

1. list  : mutable  sequence element  ==> you can changes in list . 
2. string  : immutable  sequence element  ==> you can't changes in string .
3. tuple  : immutable  sequence element  ==> you can't changes in tuple .
4. dictionary  : mutable  key-value pair  ==> you can changes in dictionary .
5. set  : mutable  unordered collection  ==> you can changes in set .
"""

# 1 . list : mutable  sequence element  ==> you can changes in list .

"""
l1=[1,2,3,4,5,6,7,9j,12.56,True] 

print(l1)
print(type(l1))
"""

# list element access though index :  start  ==> 0 
"""
l1=[1,2,3,4,5,6,7,9j,12.56,True] 

print(l1[4])
l1[2] = "viral"  # update list element though index 
print(l1)
"""

# built in function  : len  min max sorted sum 

"""
l1=[1,2,3,4,5,6,7,9,99,45] 
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to desc 
print(sorted(l1,reverse=True))  # desc to asc
print(sum(l1)) 
"""

# slicing  : 

"""
l1=[10,20,30,40,50,60,70,999,99,45] 
# start  index : 0  ==> pos  index ==> l to  r 
# neg index : -1   ==> neg index ==> r to l 

print(l1[4])
print(l1[5])
print(l1[2:6])  # 2 start  index number  6 ending index number 

print(l1[:6])
print(l1[1:])
print(l1[-2])
print(l1[-2 :-8])
print(l1[2 :-4])

print(l1[1 :8:2])# start 1  8 end index 2 step size 
print(l1[ :9:3])# start 0  9 end index 2 step size 

print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])
print(l1[-2 :-8 :-1])
l1[2:4] =[100,200]
print(l1)
"""
# method  : 

l1=[10,20,30,40,50,60,70,999,99,45,50] 

# l1.append(1000)  # add in last 
# print(l1)

# l1.clear()
# print(l1)

# l2=l1.copy()
# print(l2)

# l2=["viral","prince","jay"]
# l1.extend(l2)
# print(l1)

# print(l1.count(50))

# print(l1.index(50))
# print(l1.index(50,5,20))

# l1.pop()  
# print(l1)  # if no given arg then  pop  always remove  last element .

# l1.pop(4)
# print(l1)  # if  you given arg  then  pop remove  element from given index .

# l1.remove(20)
# print(l1)

# l1.insert(3,"jay")
# print(l1)

# l1.sort()
# print(l1)

# l1.sort(reverse=True)
# print(l1)

# l1.reverse()
# print(l1)


# task  :1 
"""
input  : l1=[10,20,30,40,50,60,70,999,99,45,50] 
ouptut : print  second  largest number in the list  ===> 99 
"""
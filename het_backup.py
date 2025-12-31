# data type  : 
"""
1. string  : immutable sequence of characters
2. list : mutable sequence of any type
3. tuple : immutable sequence of any type
4. dictionary : mutable sequence of key-value pair 
5. set : mutable  collection  of  unordered  unique  elements.
"""

# set : mutable  collection  of  unordered  unique  elements.

"""
s1={100,2,2,3,3,4,5,6,7,8,"moksh",9j,True}
print(s1)
print(type(s1))
"""

# empty set : 
"""
s1=set()
print(s1)
print(type(s1))
"""

# slicing  : 

"""
s1={100,2,2,3,3,4,5,6,7,8,True}
print(s1[3])  # not  possible  slicing  in set bcz of  unordered  unique  elements
"""

# built in function : len min max sorted sum  

"""s1={100,2,2,3,3,4,5,6,7,8,True}
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to desc
print(sorted(s1,reverse=True))  # desc to asc
print(sum(s1))
"""
# method :

# s1={100,2,2,3,3,4,5,6,7,8,True,90}

# s1.add(67)
# print(s1)

# s2=s1.copy()
# print(s2)

# s1.clear()
# print(s1)

# discard  , remove , pop : 

"""
s1.discard(100)
print(s1) 

s1.remove(1)
print(s1)

s1.pop()
print(s1)
"""

# s1={1,2,3,4}
# s2={3,5,6}
# s3={1,2,3,4,5,6,7,8}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2)) # s1-s2
# print(s1.symmetric_difference(s2))

# s1.intersection_update(s2)
# s1.difference_update(s2)
# s1.symmetric_difference_update(s2)
# print(s1)

# disjoint  , subset , superset :

"""s1={1,2,3,4}
s2={5,6,3}
s3={1,2,3,4,5,6,7,8}
"""
# print(s1.isdisjoint(s2))
# print(s2.issubset(s3))
# print(s3.issuperset(s1))
# print(s3.issuperset(s2))

# s1.update(s2)
# print(s1)

# fronzen set : immutable set that can not be changed .

"""fz = frozenset({100,2,3,3,4,5,"moksh",9j,True})
print(fz)
print(type(fz))

"""

# task :1 ask user to enter the element  store  in list and remove the duplicate using set.

"""l1=[1,1,2,2,3,3,4,4,5,6,7,8,9]
r= set(l1)
print(list(r))
"""

l2=["het","het","dhruv","moksh","dhruv"]
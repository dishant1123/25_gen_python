# set : mutable  collection  of  unordered  unique  elements.  

"""
s1={100,1,2,2,3,3,4,5,6,7,8,"moksh",9j,True}
print(s1)
print(type(s1))

"""
# empty set : 
"""
s2=set()
print(s2)
print(type(s2))
"""

# built in function  : len min max sorted sum 

"""
s1={100,1,2,2,3,3,4,5,6,7,8,False}
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to desc
print(sorted(s1,reverse=True))  # desc to asc
print(sum(s1))
"""

# remove the  duplicate  element  from list : 

"""l1=[1,2,2,3,3,4,5,5,6,7,8,8,9]
l2= set(l1)
print(list(l2))
"""

# methods : 

# s1={100,67,1,2,2,3,3,4,5,6,7,8}

"""s1.add(79)
print(s1)
"""
"""s1.clear()
print(s1)
"""

"""s2=s1.copy()
print(s2)
"""
# update :
"""s2={"moksh","prey"}
s1.update(s2)
print(s1)
"""

# remove  : 

"""s1.remove(100)
print(s1)
"""
# discard : 
"""s1.discard(100)
print(s1)

s1.discard(900)
print(s1)
"""
#pop : 

"""
s1.pop()
print(s1)
"""

# union , intersection , difference , symmetric_difference  : 

"""
s1={1,4,5}
s2={1,2,4,6,7}
s3={1,2,3,4,5,6,7,8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1-s2
print(s2.difference(s1))  # s2-s1
print(s1.symmetric_difference(s2))

s1.intersection_update(s2)
print(s1)
s1.difference_update(s2)
print(s1)
s1.symmetric_difference_update(s2)
print(s1)
"""

# disjoint  , subset , superset : 

"""s1={1,4,5,6,7,2}
s2={1,2,6,7}
s3={1,2,3,4,5,6,7,8}

print(s1.isdisjoint(s2))  
print(s2.issubset(s1))
print(s3.issuperset(s1))

"""
# frozen set : imuutable  set  that  can  not  be  changed .

"""
fz =frozenset({100,2,3,3,4,5,"moksh",9j,True})
print(fz)
print(type(fz))

"""
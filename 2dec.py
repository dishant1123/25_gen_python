#dict : mutable sequence of key-value pair .

"""
d1={"phy" :90 , "che" :56}
print(d1)
print(type(d1))

d2={56:89,"com":12}
print(d2)
print(type(d2))

"""

# add in dict : 
"""
d1={"phy" :90 , "che" :56}
d1["com"]=90 
print(d1)
"""
# slicing  : 
"""
d1={"phy" :90 , "che" :56}
print(d1[0])  # not possible  slincing in dict 
"""
# built in function  :  len  min max sorted sum

"""
d1={"phy" :90 , "che" :96}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  # asc to desc
print(sorted(d1,reverse=True))  # desc to asc
print(sum(d1))
"""

# method  : 

d1={"phy" :90 , "che" :96}

"""d1.clear()
print(d1)
"""

"""d2= d1.copy()
print(d2)
"""
"""print(d1.keys())
print(d1.values())
print(d1.items())
"""

# print(d1.get("phy"))  # arg : key 

l1=["moksh","het"]
# d2={"krishiv":90 ,"het" :90}
"""
d2 =dict.fromkeys(l1,90)
print(d2)
d2["het"]=88
print(d2)
"""
d1={"phy" :90 , "che" :96,"com":99}

# d1.pop("phy")  # arg : key   key delete 
# print(d1)

# d1.popitem()   # last key value pair 
# print(d1)

"""
d1.setdefault("ss",67) 
print(d1)
"""

# task :1 
"""
Ask user to give name and marks of 5 different students. Store them in dictionary. 

ram 90 sita 77  ravan 66 
output  :{"ram":90,"sita":77,"ravan":66}

"""

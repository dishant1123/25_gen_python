"""
pandas : pip install pandas 

use  ==> 1. data cleaning  2. data analysis  3. data visualization

ex : 

age    income    cr_score
19      89999     750 
        90000     800 
21                 600 
"""
import pandas as pd 

a =pd.Series([21,34,56,78,90,16,17])
# print(a)

"""b= pd.Series([21,34,56,78,90,16,17,92,89],index=['a','b','c','d','e','f','g','h','i'])
print(b)
print(b.head(4))  # default ==> 5 rows , fetch   ==> first  5 rows 
print(b.tail(2))  # default  ==> last 5 rows only ,  offset ==> last 
print(b.index)
"""

"""c= pd.Series([21,45,78,90,16],index =['a','b','c','d','e'])
print(c)
print(c.dtype)
print(c.index)
print(c.values)
c['a']=210 
print(c)
"""

# maths  function  : 

"""
c=pd.Series([21,45,78,90,16],dtype='int64')
print(c.sum())   # 250
print(c.mean())  # 50
print(c.min())
print(c.max())
print(c.median()) #  78 
print(c.var()) 
print(c.std())
"""
d= pd.Series(["moksh","het","vyom","rishi","saloni"],index =[1,2,3,4,5])

print(d)
print(d.drop(index =2))
print(d.drop(labels =[2,3]))

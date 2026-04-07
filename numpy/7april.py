import  numpy  as np 

# slicing  1 d array ,  2 d array  : 

"""a= np.array([1,2,3,4,5,6,7,8,9])

print(a)
print(a[6])
print(a[2 :5:2])  # start 2 index stop  5  step  2 
print(a[-1])
print(a[ : : -1])
"""
# 2 array slicing  : 
"""b= np.arange(1,17).reshape(4,4)
print(b)
print(b[1])  # 2d array :  first  element  row   ==> second element column
print(b[2])
print(b[2:4])  # 2 start  4 end 
print(b[1:3,1:3])  # 1:3 row   1:3 col 
print(b[1: 4 :2, 0 : 4: 2])
print(b[1: 4 :2,  : : -1])
"""
"""
 [ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]

"""

# 3 array slicing  :

a=np.arange(1,19).reshape(2,3,3)
print(a)

print(a[1,1,1])
print(a[0,1,1])

"""
task :1 create  a array  using   np.ones () 5*5 .  

output  : 

    [[1 1 1 1 1],
    [1 0 0 0 1],
    [1 0 9 0 1],
    [1 0 0 0 1],
    [1 1 1 1 1] ]

task :2 create  a array  using   np.arange (1,31)  ==> reshape (6,5) .

    [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]]

print only  using  slicing : 

[[11 12],
[16 17]]


task :3 create  a array  using   np.arange (1,31)  ==> reshape (6,5) .

    [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]]

output  : 

[2,8,14,20]

task :4 create  a array  using   np.arange (1,31)  ==> reshape (6,5) .

    [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]]
output : 
[[4,5], 
 [24,25],
 [29,30]]
"""


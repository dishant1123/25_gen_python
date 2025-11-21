# adv list : 
"""
l1=[1,2,3,4,5]
print(l1)
"""
# l2 =[[1,2,3],[4,5,6],[7,8,9]]
# print(l2)

"""
for i in l2 :
    print(i)
"""
"""
[1, 2, 3]    0,0 ==>1 0,1 ==>2 0,2 ==>3
[4, 5, 6]    1,0 ==> 4 1,1 ==>5 1,2 ==>6
[7, 8, 9]   
"""
"""
print(l2[0])
print(l2[0][2])
# print(l2[1][3])
print(l2[2][ : :-1])
print(l2[2][ : :-2])
print(l2[1][ : :2])

"""
# sort : 

"""l2 =[[10,2,3],
     [-4,5,6],
     [7,80,9]]

l2.sort()
print(l2)
print(sorted(l2,reverse=True))
"""

# task  :1  sort the  below  list to  second element.  
"""
l1 = [[1,3], [0,2], [5,-9]]
ouptut  : [[5,-9],[0,2],[1,3]]
"""
# bubble  sort : 

"""
l1 = [[1,3], 
      [0,2],
      [5,-9]]

n=len(l1)  #3 

for i in range(n) :  # 0-3   # 0 
    for j in range(0,n-i-1):  #  0, 2 :   # 3   > 2 
        if l1[j][1]  > l1[j+1][1] :    # l1[0][1] > l1[1][1] 2 
               l1[j],l1[j+1] =l1[j+1], l1[j]
                            # l1[0] , l1[1] =l1[1]  ,l1[0]    
print(l1)
"""

#task :2  swap first and last element. 
"""
input  : l1=[1,2,3,4,5,6,7,8]
output  :l1 =[8,2,3,4,5,6,7,1]

"""

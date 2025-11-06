"""
7. 

a
a b 
a b c 
a b c d 
a b c d e
"""
#7 :
"""ch='a'
for i in range(1,6):  # 2 
    for j in range(1,i+1):  # 2 ,3 
        print(chr(ord(ch)+j-1),end=" ")  # a 
    print()                              # a b 
"""

""" 
8.         9.         10.           11.        12.
* * * * *  * * * * *         *       *
  * * * *   * * * *        * *      * * 
    * * *    * * *       * * *     * * *
      * *     * *      * * * *    * * * * 
        *      *     * * * * *   * * * * * 
"""
#8: 
"""for i in range(1,6):  # 1 
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(5,i-1,-1):  # 1 ,1  
        print("*",end=" ")
    print()
"""
#9: 
"""
for i in range(1,6):  # 1 
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):  # 1 ,1  
        print("*",end=" ")
    print()
"""
#10 : 
"""
for i in range(1,6):  # 1 
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):  # 1 ,1  
        print("*",end=" ")
    print()
"""

#11: 
"""

for i in range(1,6):  # 1 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):  # 1 ,1  
        print("*",end=" ")
    print()
"""

#12: diamond : 

for i in range(1,6):  # 1 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):  # 1 ,1  
        print("*",end=" ")
    print()
for i in range(1,6):  # 1 
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):  # 1 ,1  
        print("*",end=" ")
    print()
"""
     1
    1 2
   1 2 3 
  1 2 3 4
 1 2 3 4 5
  1 2 3 4
   1 2 3
    1 2
     1
"""
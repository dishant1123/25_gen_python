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

"""for i in range(1,6):  # 1 
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
    print()"""
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

"""
13.         14.           15 :         16 :
 
* * * * *    *            * * * * *       * 
*       *    * *          *     *        * *
*       *    *   *        *   *         *   *
*       *    *     *      * *          *     *
* * * * *    * * * * *    *           *       * 
                                       *     * 
                                        *   *
                                         * *
                                          *
"""

#13 : 

"""for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5: 
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

#14 :
"""for i in range(1,6):  # 1 
    for j in range(1,i+1):  # 1 ,1  
        if j==1 or i==5 or i==j:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

#15 : 
"""for i in range(1,6):  # 1 
    for j in range(5,i-1,-1):  # 1 ,1  
        if i==1 or j==1 or i==j or j==5:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

# 16 : HW 

# while  loop  : 

"""
syntax : 

i= intial value 

while con : 
    print(i)
    inc/dec 
"""

# 1-100 : 

"""
i=1 
while i<=100 :
    print(i,end=" ")
    i+=1
"""

# break : 

"""
for i in range(10):
    if i==5 :
        break 
    print(i)
"""
# contunie : 

"""
for i in range(10):
    if i==5 :
        continue 
    print(i)
"""

# pass : 
"""for i in range(10):
    if i==5 :
        pass 
    print(i)
"""

# mcq :

"""for i in range(1,10): 
    if i==5 :
        continue 
    print(i)
else :
    print("hello") 
"""
"""
a. 1 2 3 4 6 7 8 9 "hello"
b. 1 2 3 4 5 6 7 8 9 "hello"
c. 1 2 3 4 6 7 8 9
d. none 
"""

"""if 5.0 == 5 :
    print("TRUE")
else :
    print("FALSE")
"""

# while True  : 

"""
syntax : 

i=intial value
while True :
    print(i)
    if  con :
        break
"""

#1-100 : 
"""i=1 
while True :
    print(i,end=" ")
    i+=1
    if i==100 :
        break
"""

"""a=int(input("enter  the  number 1:"))
b=int(input("enter  the  number 2:"))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulo")
print("6.floor  division")
choice=int(input("enter  the  operation  :"))

match choice :
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3 :
        print(a*b)
    case 4 :
        print(a/b)
    case 5 :
        print(a%b)
    case 6 :
        print(a//b)
"""
# task :1 
"""
1.exit  condition   ==> 7 
2.user  ==> 8  ==> enter the new number  : 
"""



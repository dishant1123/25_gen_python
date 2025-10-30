# nested loop  :

#amg : 

"""
start = int(input("enter the  start number  : "))
end=int(input("enter the  end number  : "))

for i in range(start ,end +1):   # 101  10000 
    sum =0 
    digits =len(str(i))   # 3 
    temp =i    # temp  =101 
    for j in range(digits):
        r= temp %10 
        sum = sum +pow(r,digits)
        temp  = temp //10 
    if sum == i : 
        print(i,end=" ")
"""
   
# strong  : 
"""
145 : 
each  digit factorial  : 1! = 1  5! = 1*2*3*4*5 =120  4! = 24 
sum = 1+120 +24 =145   ==>strong
"""

"""n=int(input("enter the  number : "))
sum = 0 
digits = len(str(n))
temp =n 
for i in range(digits):
    r = n %10    # 145 %10 =5 
    fact =1 
    for j in range(1,r+1):
        fact = fact *j 
    sum =sum +fact
    n = n //10 
if sum ==temp:
    print("strong") 
"""
# strong  number in range : 

"""start = int(input("enter the  start number  : "))
end=int(input("enter the  end number  : "))

for i in range(start, end+1):  # 101   100000 
    sum =0 
    digits =len(str(i))   # 3
    temp =i 
    for j in range(digits):
        r = temp %10 
        fact =1 
        for k in range(1,r+1):
            fact =fact *k 
        sum =sum +fact 
        temp =  temp //10 
    if sum ==i : 
        print(i,end=" ") 
"""
# pelindrome   in range  :    ==> 100  100000 

# pattern  : 
""" 
1.         2.         3.          4.          5.           6.         7. 
* * * * *  *          * * * * *   1            5 4 3 2 1   1 2 3 4 5  a 
* * * * *  * *        * * * *     1 2          5 4 3 2     2 3 4 5    a b 
* * * * *  * * *      * * *       1 2 3        5 4 3       3 4 5      a b c 
* * * * *  * * * *    * *         1 2 3 4      5 4         4 5        a b c d
* * * * *  * * * * *  *           1 2 3 4 5    5           5          a b c d e

"""
#1 : 
"""
for i in range(1,6):  # 1 
    for j in range(1,6):  # 1 
        print("*",end=" ")
    print()
"""
#2 : 
"""
for i in range(1,6):  # 1 
    for j in range(1,i+1):  # 1 ,1  
        print("*",end=" ")
    print()
"""
#3 : 

for i in range(1,6):  # 1 
    for j in range(5,i-1,-1):  # 1 ,1  
        print("*",end=" ")
    print()

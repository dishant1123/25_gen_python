# index , rindex , find , rfind : 
"""
s1="my name is yana."

print(s1.index('a'))
print(s1.index('a',5,20))
print(s1.index('a',13,20))

print(s1.rindex('a'))  # right to left 
print(s1.rindex('a',2,12))  # right to left

print(s1.find('a'))  
print(s1.find('a',5,20))
print(s1.find("ya"))
print(s1.find("me"))

print(s1.rfind('a'))  # right to left
print(s1.find('a',13,20))
"""
# spilt , rsplit , partition , rpartition  :
"""
s1="my name is moksh."


print(s1.split())  # list ===> space spilt   
print(s1.split('a'))
print(s1.split('is'))

print(s1.rsplit()) 
print(s1.rsplit('o')) 

#  hw :find  out  the  difference  between  split  and  rsplit . 

print(s1.partition('is'))   # string  ==> 3 parts 
print(s1.partition('a'))    
print(s1.partition())
print(s1.partition(" "))

print(s1.rpartition('s'))   # string  ==> 3 parts
print(s1.rpartition('my'))   # string  ==> 3 parts
print(s1.rpartition(" ",2))  # error bcz partition  only take one arg. 
"""

# count , replace  : 
s1 = "my name is  ram patel."

print(s1.count('a'))
print(s1.count('a',10,20))  # 3 arg  : count ,  start ,end 
print(s1.count('ra'))

print(s1.replace("ram","yana"))
print(s1.replace(" ",""))
print(s1.replace(" ","",1))
print(s1.replace(" ","",2))

"""
task :1   
print all 'o' index number in the  string. 
input : "i am going to  goa next month."
output : 
        first 'o' index number is  : 6 
        second 'o' index number is  : 14
        
task :2 
ask user to enter the string  and  print  count  words , len and  max words in the  string. 

input  : "i love python programming language."
output  : 
         count  words : 5
         len  : 35 
         max words : programming 

       
task :3 
ask  user  to enter the  string  and  replace the  space with  '-'  and  print the  string.
but first  space and  last space should  be replaced.

input  : "i love python programming language."
output  : i_love python programming_language.

"""


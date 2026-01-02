# index ,r index , find,r find

s1="my name is het thakkar."

"""print(s1.index("i"))
print(s1.index("het"))
print(s1.index("a"))
print(s1.index("a",18,30))

print(s1.find("i"))
print(s1.find("het"))
print(s1.find("a"))

print(s1.rindex("a"))
print(s1.rindex("a",10,19))

print(s1.rfind("a"))
print(s1.rfind("a",10,19))
"""

# task  :1 
"""
input  : "i am going to goa next month." 
output  : first o index number :6
         2 nd o index number : 12
         3 rd o index number : 15
         4 th o index number : 24
"""

# split r spilt : 

"""s1="my name is het thakkar."

print(s1.split())
print(s1.split("i"))
print(s1.split("a"))

print(s1.rsplit("a"))
"""
# hw  : diffrence between split and rsplit. 

# partition, r partition :

"""s1="my name is het thakkar."

print(s1.partition("i"))
print(s1.partition("a"))
print(s1.partition("het"))

print(s1.rpartition("a"))
"""

# task  :2 
"""
Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.
For Example:-
Input:-This is the python program
Output:-No of Words=5
	    No of letters=26(including whitespace)
	    Longest Word=program

"""

s1="this is the python program"
letters = len(s1)
words =s1.split()  # ["this","is","the","python","program"]

longest_word = max(words, key=len)
print(longest_word)
print(len(words))
print(letters)

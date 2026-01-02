#  join : 

"""s1=["my","name","is","het","thakkar."]
#my name is het thakkar.

s2=" ".join(s1)
print(s2)
"""

# islower , isupper , isalpha , isdigit , isspace , istitle , isalnum , isdecimal , isnumeric :

"""s1="My Name Is Het Thakkar."
print(s1.islower())
print(s1.isupper())
print(s1.istitle())
"""

s2 ="mokshpatel"
print(s2.isalpha())

s3="moksh28july"
print(s3.isalnum())

# isdecimal , isnumeric  ,isdigit:
"""s_digits = "12345"
print(f"'{s_digits}'.isdecimal(): {s_digits.isdecimal()}") # Output: True
print(f"'{s_digits}'.isdigit():   {s_digits.isdigit()}")   # Output: True
print(f"'{s_digits}'.isnumeric(): {s_digits.isnumeric()}") # Output: True
print("-" * 20)
"""
# Superscript (Unicode U+00B2)
# s_superscript = "10²"
# print(f"'{s_superscript}'.isdecimal(): {s_superscript.isdecimal()}") # Output: False
# print(f"'{s_superscript}'.isdigit():   {s_superscript.isdigit()}")   # Output: True
# print(f"'{s_superscript}'.isnumeric(): {s_superscript.isnumeric()}") # Output: True

# print("-" * 20)

# # Vulgar Fraction (Unicode U+2153)  
"""s_fraction = "5¼"
print(f"'{s_fraction}'.isdecimal(): {s_fraction.isdecimal()}") # Output: False
print(f"'{s_fraction}'.isdigit():   {s_fraction.isdigit()}")   # Output: False
print(f"'{s_fraction}'.isnumeric(): {s_fraction.isnumeric()}") # Output: True

note  : not  including vulgar function  ==> isdigit ,isdecimal ==> false
"""
# print("-" * 20)

# # String with non-numeric characters (space or period)
"""
s_float = "125"
print(f"'{s_float}'.isdecimal(): {s_float.isdecimal()}") # Output: False
print(f"'{s_float}'.isdigit():   {s_float.isdigit()}")   # Output: False
print(f"'{s_float}'.isnumeric(): {s_float.isnumeric()}") # Output: False
"""

"""
task  :4 take list from user append all element in list and print pelindorme word in list  
         input : ["java", "python", "php","cpp","flutter","maam"]
         output :  ['php','maam']

task  : 6 Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2


task  : 10 
	Write a Python program to find the length of a given list of non-empty strings.
	Input:
	['cat', 'car', 'fear', 'center']
	Output:
	[3, 3, 4, 6]
	Input:
	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
	Output:
	[3, 3, 7, 5, 2, 4, 0]

"""

# hw : 
"""
ask user to create password  condition :
    1.password len ==> min 8
    2.1 upper case 1 lower case 1 digit 1 special char
    
example :
    password : moksh1211   ==> wrong  ==> special char, upper  
    
    password : Moksh1211   ==> wrong  ==> special char 
    password : Moksh1211!  ==> coorect
   
hint  : isdigit() , islower() ,isupper() , isalpha() , isalnum()
"""


# task :1 
"""
Ask user to give name and marks of 5 different students. Store them in dictionary. 

ram 90 sita 77  ravan 66 
output  :{"ram":90,"sita":77,"ravan":66}

"""

# task  :2 above  dict  sorted by values . 

d1={}
for i in range(3):
    name =input("enter the name  : ")
    marks =int(input("enter the marks :"))
    d1[name] =marks
print(d1) # {'ram': 90, 'sita': 56, 'ravan': 34}

sorted_marks = sorted(d1.values())  # [34,56,90]
d2={}
for i in sorted_marks: #[34,56,90]
    for j,k in d1.items() : #{'ram': 90, 'sita': 56, 'ravan': 34}
        if i ==k : 
            d2[j] =k 
print(d2)

# task :3  sorted by  keys . 

# task  :4 
"""
ask user to enter the  string  and  count the letter and store in dict.
input  : "mississippi"
output : {'m':1,'i':4,'s':4,'p':2}
 
"""
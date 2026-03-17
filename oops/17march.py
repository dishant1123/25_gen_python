# file handling :
"""
r+ :  read + write ==> exiting file   
w+ :  read + write  ==> new file  create  ==> exiting file + overwrite
a+ :  read + append ==> new file  create  ==> exiting file + last add
"""

# ex :1 read + 

"""with open("het.txt","r+") as f : 
    f.write("pinal patel.")
    f.seek(0)  # to move cursor to start of file
    c=f.read()
    print(c)
    f.close()
"""    
# het loves rcb.  ==> 14   "pinal patel." ==> 12

# ex :2 write +

"""with open("moksh.txt","w+") as f :
    f.write("moksh is  cool boy.\n")
    f.seek(0)
    c=f.read()
    print(c)
    f.close()
"""

"""with open("pinal.txt","w+") as f :
    f.write("my name is pinal.\n")
    f.write("study in OLD LJ. \n")
    f.write("very intelligent.\n")
    f.write("she help everyone  in class for exam .\n")
    f.seek(0)
    c=f.readline()
    print(c)
    f.close()
"""

# append + 

"""with open("pinal.txt","a+") as f :
    # f.write("live in ahmedabad.\n")
    f.seek(0)
    c=f.read()
    print(c)
    f.close()
"""

# task :1 
"""
ask user to enter the string  and seprate  vowel and consonant and print  seprate file vowel.txt and consonant.txt. 

input  : my name is het thakkar. 
output  : 
    vowel.txt : ae i e aa. 
    consonant.txt : my nm s ht thkkr.
"""

s=input("enter the string  : ")  # my name is het thakkar.

for i in s : 
    if i in "aeiouAEIOU" :
        with  open("vowel.txt","a+") as f :
            f.write(i)
            f.close()
    else : 
        with  open("consonant.txt","a+") as f :
            f.write(i)
            f.close()
# number  guessing game  : 
"""
number  ==> computer  guess ==> range   ==> 1,20   ==> guess = 15 
             
user total attempt =4 
1 attempt :6   2 attempt : 14   3 attempt : 15 
congrats   !!!  you win 

logic :  
1. loop        
2. if (con) : user_num > guess_num   : too  high 
3. if (con) : user_num < guess_num   : too low 

else :  you win  

print("u  loss",computer_guess) 

"""
import  datetime 

"""a= datetime.datetime.now()
print(a)
"""
"""
string format : 
"""
"""b= datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
print(b)

t= datetime.datetime.today()
print(t)
"""
# customize  format : 
"""a= datetime.datetime(2026,2,3,6,30,45,12345)
print(a)
print(a.day)
print(a.month)
print(a.year)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
"""
# time  format  : 

import  time  

"""a=time .time()
print(a)

b=time.ctime()
print(b)

c=time.localtime()
print(c)
"""
"""
for i in range(10):
    time.sleep(0.50)
    print(i)
"""

from datetime import  timedelta 

"""today = datetime.datetime.now()
futuredate= today + timedelta(days =165)

print("today : ",today)
print("futuredate",futuredate)
"""

import calendar 

"""
c=calendar.month(2026,3)
print(c)

d=calendar.calendar(2026)
print(d)
"""
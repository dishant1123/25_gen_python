"""
Write a Python program to implement a Movie Ticket Booking System using lists and functions.

The program should provide the following menu:
1. Add Movie
2. Book Ticket
3. Search Movie
4. Display Movie List
5. Exit

Movie Details:
- Movie ID (unique)
- Movie Name
- Available Seats
- Timing Slot

While booking tickets, display the following ticket categories:
- Gold : 450
- Silver : 650
- Platinum : 800
Generate a bill after successful ticket booking.
"""

movie_id=[]
movie_name=[]
seats =[]
timing =[] 

def is_unique(mid):
    return mid not  in movie_id
    
def add_movie() : 
    mid =int(input("enter the movie id : "))
    
    if not is_unique(mid):
        print("movie id already exists")
        return 
    name =input("enter the movie name : ")
    seat =int(input("enter the movie seats : "))
    time =input("enter the movie timing : ")  # ex : 9pm 9am 10 pm 10am 
    
    movie_id.append(mid)
    movie_name.append(name)
    seats.append(seat)
    timing.append(time)
    print("movie added successfully")
    
def book_ticket(): 
    mid=int(input("enter the movie id : "))
    
    if mid not in movie_id:
        print("movie not found")
        return 
    
    index =movie_id.index(mid)
    
    print("movie name : ",movie_name[index])
    print("available seats : ",seats[index])
    print("timing : ",timing[index])
    
    print("Ticket Categories \n")
    print("Gold : 450")
    print("Silver : 650")
    print("Platinum : 800")
    
    choice =int(input("enter the ticket category : "))
    if choice == 1:
        price =450 
        category ="Gold"
    elif choice == 2:
        price =650
        category ="Silver"
    elif choice == 3:
        price =800
        category ="Platinum"
    else :
        print("invalid choice")
        return 
    qty =int(input("enter the quantity : "))
    
    if qty >seats[index]:
        print("not enough seats")
        return
    
    seats[index] -= qty
    total =qty*price
    
    print("Movies Bill : \n")
    print("Movie Name : ",movie_name[index])
    print("Movie Seats : ",seats[index])
    print("Timing : ",timing[index])
    print("Ticket Category : ",category)
    print("Quantity : ",qty)
    print("Price : ",price)
    print("Total  bill: ",total)

def search_movie():
    
def display_movie():
    
def main(): 
    
# add_movie()
# add_movie()

# book_ticket()

# print(movie_id)
# print(movie_name)
# print(seats)
# print(timing)

    
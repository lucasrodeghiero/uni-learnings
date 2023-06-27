newBook = int(input("Please enter amount of new books: "))
oldBook = int(input("Please enter amount of old books: "))
rentBook = int(input("Please enter the amount of books you would like to rent: "))
daysRent = int(input("Please enter the amount of days you would like to rent: "))
rent = rentBook*(daysRent*2)

print(f'Your total expense is: ${newBook*10+oldBook*4.50+rent:.2f}')

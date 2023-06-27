from order import Order

print("----------Enter following details to print an order form----------")

myCode = input("Enter ISBN code: ")
myTitle = input("Enter title of the book: ")
myAuthor = input("Enter author/s of the book: ")
myPrice = float(input("Enter price of a book: $"))
myNumber = int(input("Enter number of books to order: "))

total = myPrice*myNumber

print(f"\n\n\nBOOK ORDER PLACED FOR ISBN: {myCode}\n----------------------------------")
finalOrder = Order(myCode,myTitle,myAuthor,myPrice,myNumber,total)
print(finalOrder)

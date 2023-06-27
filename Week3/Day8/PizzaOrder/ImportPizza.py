from pizzaorder import PizzaOrder

myFlavour = input("Enter the flavour: ")
mySize = input("Enter the size: (Small, Large, Medium) ").lower()
pNumber = int(input("Enter number of pizzas: "))

myOrder = PizzaOrder(myFlavour,mySize,pNumber) #instance
print(myOrder)

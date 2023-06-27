from mutator import Mutator

myFlavour = input("Enter the flavour: ")
mySize = input("Enter the size (Small, Medium, Large): ").lower()
pNumber = int(input("Enter number of pizzas: "))

myPizza = Mutator()
myPizza.setName(myFlavour)
myPizza.setSize(mySize)
myPizza.setNumber(pNumber)

print(myPizza)

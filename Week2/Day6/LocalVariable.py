#Global variable
a = 5
b = 8
myList = [90, 65, 12, 82]

#C and total are local variables
def addValues():
    c = 50 + len(myList)
    total = a + c
    return total
#Product is a local variable
def multValues():
    product = b * len(myList)
    return product
#finalTotal is a local variable
def main():
    finalTotal = addValues() + multValues()
    myList.append(finalTotal)
    print(myList)
main()

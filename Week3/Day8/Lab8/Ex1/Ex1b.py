from storage import Storage

myLength = float(input("Enter the storage floor length: "))
myWidth = float(input("Enter the storage floor width: "))
myHeight = float(input("Enter the storage floor height: "))

po1 = Storage()
po1.setLength(myLength)
po1.setWidth(myWidth)
po1.setHeight(myHeight)
print(po1)

from storagecontainer import StorageContainer

myLength = float(input("Enter the storage floor length: "))
myWidth = float(input("Enter the storage floor width: "))
myHeight = float(input("Enter the storage floor height: "))

myArea = StorageContainer(myLength,myWidth,myHeight)

print(myArea)

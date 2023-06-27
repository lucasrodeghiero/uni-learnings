"""
Standard delivery fee of $15
Orders over $100 no delivery fee

ADULT - 20kg -  100  LARGE
ADULT - 15kg -  70   MEDIUM
ADULT - 5kg  -  40   SMALL

PUPPY - 20kg -  95 - LARGE
PUPPY - 15kg -  65 - MEDIUM
PUPPY - 5kg  -  35 - SMALL

3 INPUTS FROM THE USER
BAG SIZE (USER CAN INPUT LOWER AND UPPERCASE)
DOG SIZE
QUANTITY OF BAGS


"""
size = dog = price = 0
bagSize = input('Please choose your bag size: 20kg (Large), 15kg (Medium), 5kg (Small): ')
if bagSize == 'L' or bagSize == 'l':
    size = 'Large'
    price = 100.00
elif bagSize == 'M' or bagSize == 'm':
    size = 'Medium'
    price = 70.00
elif bagSize == 'S' or bagSize == 's':
    size = 'Small'
    price = 40.00
else:
    print('Please enter the correct bag size.')

dogSize = str(input('Is it an ADULT dog or PUPPY dog (A/P)? '))
if dogSize == 'A' or dogSize == 'a':
    dog = 'Adult'
elif dogSize == 'P' or dogSize == 'p':
    dog = 'Puppy'
else:
    print('Please enter valid data.')
bagQuantity = int(input(f"How many bags of {size} size bags? "))
#Order details
print('Order Details\n****************')
print(f'Food type: {dog}')
print(f'Bag size: {size}')
print(f'Number of bags: {bagQuantity}')
if dog == 'Puppy':
    totalCost = price*bagQuantity -(5*bagQuantity)
    if totalCost > 100:
        print(f'Total amount with delivery: ${totalCost :.2f}')
    else:
        print(f'Total amount with delivery: ${totalCost+15 :.2f}')
else:
    totalCost = price*bagQuantity
    if totalCost > 100:
        print(f'Total amount with delivery: ${totalCost :.2f}')
    else:
        print(f'Total amount with delivery: ${totalCost+15 :.2f}')



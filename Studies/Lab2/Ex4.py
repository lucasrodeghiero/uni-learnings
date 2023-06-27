bagSize = input("Please enter bag size: (20kg, 15kg, 5kg)\n\t\t  Large(L), Medium(M), Small(S): ")
dogType = input("Adult or Puppy (A/P): ")
size = type = price = totalCost= 0
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
    print('Not a valid size')

bagQuantity = int(input(f'How many bags of {size} size bags: '))


if dogType == 'a' or dogType == 'A':
    type = 'Adult'
    totalCost = bagQuantity*price
elif dogType == 'P' or dogType == 'p':
    type = 'Puppy'
    totalCost = bagQuantity*(price-5)
else:
    print('Not a valid size')
print('Order Details\n***************')
print(f'Food Type: {type}')
print(f'Bag size: {size}')
print(f'Number of bags: {bagQuantity}')
if totalCost > 100:
    print(f'Total amount with delivery: ${totalCost:.2f}')
else:
    print(f'Total amount with delivery: ${totalCost+15:.2f} ')



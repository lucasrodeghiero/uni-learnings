bagSize = str(input('Bag size 20kg (Large), 15kg (Medium), 5kg(Small): '))
if bagSize == 'L' or 'l':
    size = 'Large'
    price = 100.00
elif bagSize == 'M' or 'm':
    size = 'Medium'
    price = 70.00
elif bagSize == 'S' or 's':
    size = 'Small'
    price = 40.00
else:
    print('Please enter a valid size.')
foodType = input('For adult dog or puppy dog (A/P): ')
if foodType == 'A' or 'a':
    dogSize = 'Adult'
if foodType == 'P' or 'p':
    dogSize = 'Puppy'
else:
    print('Enter a valid size.')
amount = str(input(f'How many bags of {size} size bags? '))












"""
adultLarge = 100
puppyLarge = 95
adultMedium = 70
puppyMedium = 65
adultSmall = 40
puppySmall = 35

deliveryFee = 15

pupAdult = str(input('For adult dog or puppy dog (A/P): '))


totalAmount = foodType*bagSize*bagsNumber

"""

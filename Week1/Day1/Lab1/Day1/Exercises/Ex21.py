vegetarian = 11.80
meat = 12.80
seafood = 14.00
vegSale = int(input('How many Vegetarian Meals did you order? '))
meatSale = int(input('How many Meat Meals did you order? '))
seafoodSale = int(input('How many Seafood meals did you order? '))
totalOrder = (vegSale*vegetarian) + (meatSale*meat) + (seafoodSale*seafood)
print(f'Your total expense was: ${totalOrder : .2f}')

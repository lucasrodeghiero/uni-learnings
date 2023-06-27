price = float(input('Please enter the price of a drink can: '))
canQuantity = int(input('Please enter the number of cans in the pack: '))
#Standard service charge of $1
totalCost = (price*canQuantity)+1
print(f'Your order has a total price of: ${totalCost :.2f}')

fiveStems = int(input('How many 5 stem bunches? '))
tenStems = int(input('How many 10 stem bunches? '))
individual = int(input('How many individual flower stems? '))


totalCost = fiveStems*10 + tenStems*15 + individual*2

if totalCost > 50:
    print(f'Your total is: $ {totalCost :.2f}')
    print('You get 2 free flowers to choose')
else:
    print(f'Your total is: $ {totalCost :.2f}')

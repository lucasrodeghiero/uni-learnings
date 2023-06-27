slabCost = 85
width = float(input('Please enter the width: '))
lenght = float(input('Please enter the lenght: '))
area = float(width) * float(lenght)
areaSlab = float(slabCost) * float(area)
print(f'The total area to be slabbed is: {area} square metres.')
print(f'The total cost will be ${areaSlab : .2f}.')

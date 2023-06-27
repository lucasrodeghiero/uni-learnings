length = float(input('Length of the area to be paved (m): '))
width = float(input('Width of the area to be paved (m): '))
decEdge = float(input('Width of the decorative edge (m): '))

totalArea = length*width
lengthEdge = length - 2*decEdge
widthEdge = width - 2*decEdge
decorativePaving = totalArea - (lengthEdge*widthEdge)
straightPaving = totalArea - decorativePaving
print('Areas\n******')
print(f'The straight paving area is: {straightPaving:.2f} square metres')
print(f'The decorative paving area is: {decorativePaving:.2f} square metres.')

print('Costs for areas\n**************')
print(f'The price for straight paving area is: ${straightPaving*100:.2f}')
print(f'The price for decorative paving area is: ${decorativePaving*150:.2f}')

print('Total cost for paving\n*****************')
print(f'The total price for paving is: ${straightPaving*100+decorativePaving*150:.2f}')

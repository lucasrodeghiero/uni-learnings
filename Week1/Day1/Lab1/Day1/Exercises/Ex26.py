"""straightPaving = 100
edgePaving = 150

straight paving = 6 - 2*0.5 = 5
straight paving = 4 - 2*0.5 = 3
total lenght = 6*4

decorative = total - decorative = 24 - 15


"""
lenght = float(input('Please provide lenght of the area to be paved (m): '))
width = float(input('Please provide width of the area to be paved (m): '))
decEdge = float(input('Please provide width of the decorative edge (m): '))

#Areas
totalArea = float(lenght*width)
straightArea = float((lenght-decEdge*2)*(width-decEdge*2))
decArea = float(totalArea - straightArea)
print(f'The straight paving area is: {straightArea:.2f} square metres.')
print(f'The decorative paving area is: {decArea:.2f} square metres.')

#Cost for areas
straightAreaCost = straightArea * 100
decAreaCost = decArea *150
print(f'The price for straight paving area is $: {straightAreaCost:.2f} ')
print(f'The price for decorative paving area is $: {decAreaCost:.2f} ')

totalCost = float(straightAreaCost+decAreaCost)
print(f'The total price for paving is $: {totalCost:.2f}')

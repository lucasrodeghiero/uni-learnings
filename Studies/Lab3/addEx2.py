itemCost = float(input("Enter the cost of the item: "))
itemType = str(input("Air Con(AC)/Gas Heater(GH)/Dish Washer(DW)/Washing Machine(WM): "))
numYears = int(input("Enter the number of years to depreciate the item: "))

print(f'{"Years":>4}\t{"Current Value":>10}{"Depreciation Value":>20}{"Future Value":^20}')

if itemType == 'AC' or itemType == 'ac' or itemType == 'GH' or itemType == 'gh':
    depRate = 0.10
else:
    depRate = 0.05
depValue = 0
for count in range(1,numYears+1):
    depValue = itemCost - (itemCost*depRate)
    print(f'{count:>4} {itemCost:>10.2f} {itemCost-depValue:>20.2f} {itemCost-itemCost*depRate:^20.2f}')
    itemCost = depValue

print(f'The depreciation rate is: {depRate:.2f}')
print(f'The total depreciation after {numYears} years: $')
print(f'The future value of item after {numYears} years: ${itemCost:.2f}')

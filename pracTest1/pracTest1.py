"""
Lucas do Amaral
02/03/2022
"""

#Inputs
furnishCost = int(input("Please enter the total cost to furnish $: "))
flatType = str(input("Large or Small apartment? (L - Large/S - Small): "))
schedYear = int(input("Enter number of years for the schedule: "))

#Header
print(f'{"Year":>4} {"Depreciation":>15} {"Currently Valued at $":>25}')

#Depreciation Rate
if flatType == 'L' or flatType == 'l':
    depRate = 0.10
else:
    depRate = 0.08

#Declaring Undefined Variables
count = currentDep = totDepreciation = 0

for count in range(1,schedYear+1):
    currentDep = furnishCost*depRate
    totDepreciation += currentDep
    print(f'{count:>4} {currentDep:>15.2f} {furnishCost-currentDep:>25.2f}')
    furnishCost = furnishCost-currentDep
print(f'Content depreciation rate: {depRate:.2f}')
print(f'Total depreciation at the end of schedule: ${totDepreciation:.2f} ')

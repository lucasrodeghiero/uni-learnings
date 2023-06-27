propRenoValue = int(input('Property/Renovation value: '))
depRate = float(input('Depreciation rate (%) applicable: '))
numYears = int(input('Number of years to depreciate: '))

print('Investment Property Depreciation')

rate = depRate/100

depValue = 0
print(f'{"Year":>4} {"Current Value":^20} {"Depreciated Value":>20} {"Depreciation":>20}')
for count in range(1,numYears+1):
    depValue = propRenoValue - (propRenoValue*rate)
    print(f'{count:>4} {propRenoValue:^20.2f} {depValue:>20.2f} {propRenoValue-depValue:>20.2f}')
    propRenoValue = depValue

print(f'The depreciation rate used: {rate:.3f}')
print(f'Current property value: ${depValue:.2f}')

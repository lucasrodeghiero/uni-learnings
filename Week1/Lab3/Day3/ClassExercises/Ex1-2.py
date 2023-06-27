renoValue = float(input('Property/renovation value: '))
depRate = float(input('Please input depreciation rate (%) applicable: '))
years = int(input('Number of years to depreciate: '))

ratePerc = depRate/100
print()

print(f'{"Year":>4} {"Current Value":^20} {"Depreciated Value":>20} {"Depreciation":>20}')
investment = 0
for count in range(1,years+1):
    investment = renoValue - (renoValue*ratePerc)
    print(f'{count:>4}{renoValue:^20.2f}{investment:>20.2f}{renoValue-investment:>20.2f}')
    renoValue = investment
print(f'The depreciation rate used: {ratePerc}')
print(f'Current property value: {investment:.2f}')




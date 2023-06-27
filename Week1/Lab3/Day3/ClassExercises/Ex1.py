investMent = float(input('Property/renovation value: '))
depreciation = float(input('Please input depreciation rate (%) applicable: '))
years = int(input('Number of years to depreciate: '))

depreciation_rate = depreciation/100
print()

print(f'{"Year":<4}{"Value after depreciation":>30}')

#lowbound starts at 1 and upbound we will use our years + 1
for count in range(1, years+1):
    newInvestment = investMent - (investMent * depreciation_rate)
    print(f'{count:>2} {newInvestment:>22.2f}')
#has to be updated for next calculation
    investMent = newInvestment

print(f'\nThe depreciation rate used: {depreciation_rate:.2f}')


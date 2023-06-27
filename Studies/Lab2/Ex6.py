firstInt = int(input('Please enter first integer: '))
secInt = int(input('Please enter second integer: '))

if firstInt != secInt:
    print(f'{firstInt} is not equal to {secInt}')
else:
    print(f'{firstInt} is equal to {secInt}')
if firstInt >= secInt:
    print(f'{firstInt} is greater than or equal to {secInt}')
else:
    print(f'{firstInt} is less than {secInt}')
if firstInt <= secInt:
    print(f'{firstInt} is less than OR equal to {secInt}')
else:
    print(f'{secInt} is less than OR equal to {firstInt}')

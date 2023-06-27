first = int(input('Please enter first integer: '))
second = int(input('Please enter second integer: '))

if first != second:
    print(f'{first} is not equal to {second}')
else:
    print(f'{first} is equal to {second}')
if first >= second:
    print(f'{first} is greater than or equal to {second}')
else:
    print(f'{first} is less than {second}')
if first <= second:
    print(f'{first} is less than OR equal to {second}')
else:
    print(f'{second} is less than OR equal to {first}')


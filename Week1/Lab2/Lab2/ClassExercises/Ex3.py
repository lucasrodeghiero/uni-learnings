num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your first number: '))
if num1 > num2:
    difference = num1 - num2
    print(f'The difference is {difference}')
elif num2 > num1:
    addition = num2 + num1
    print(f'This is the addition of the two number: {addition}')
else:
    print('Your numbers are equal.')


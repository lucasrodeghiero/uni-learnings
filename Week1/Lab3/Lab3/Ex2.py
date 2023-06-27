num = int(input('Please input a whole number: '))
rows = int(input('How many rows in the table? '))

#Produce table heading
print(f'Multiplication of {num}')

for count in range(1,rows+1):
    mult = num * count
    print(f'{rows:>3} x {num:>3} = {mult:>4}')

num = int(input("Please input a whole number: "))
rows = int(input("Hpw many rows in the table? "))

#produce table heading

print(f'Multiplication of {num}')
for count in range(1, rows+1):
    mult = num*count
    print(f'{count:>5} x {num:^4} = {mult}')

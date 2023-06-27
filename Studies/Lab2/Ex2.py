category = int(input('Please enter your category from 1 to 3: '))
salary = float(input('Please enter your salary: '))
if category == 1:
    print(f'Your bonus is equal to: ${salary*1.02/12:.2f}')
elif category == 2:
    print(f'Your bonus is equal to: ${salary*1.05/12:.2f}')
else:
    if category == 3:
        print(f'Your bonus is equal to: ${salary*1.1/12:.2f}')

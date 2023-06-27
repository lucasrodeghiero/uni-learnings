# 3 job categories
salary = int(input('Please enter your salary: $ '))
while(True):
    category = int(input('Please enter your category: '))
#LIMITING NUMBER OF ENTRIES
    if 1 <= category > 4:
        print('Enter a valid number from 1 to 3 to choose your category!')
    else:
       break
if category == 1:
    print(f'${salary*1.02/12 :.2f} is your bonus.')
elif category == 2:
    print(f'${salary*1.05/12 :.2f} is your bonus.')
else:
    print(f'${salary*1.1/12 :.2f} is your bonus.')

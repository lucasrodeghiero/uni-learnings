while(True):
    month = int(input('Enter the month as a number (eg: January = 1): '))
    if month > 12:
        print('Enter a valid number from 1 to 12 to enter you grade!')
    else:
        break
if month == 3 or month == 4 or month == 5:
    print('This is Autumn season')
elif month == 6 or month == 7 or month == 8:
    print('This is Winter season')
elif month == 9 or month == 10 or month == 11:
    print('This is Spring season.')
else:
    print('This is summer')

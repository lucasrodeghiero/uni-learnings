wkHours = float(input('Please enter the amount of hours you have worked: '))
if wkHours > 38:
    overTime = wkHours - 40
    print(f'Pay overtime for {overTime} hours.')
else:
    print('No overtime')

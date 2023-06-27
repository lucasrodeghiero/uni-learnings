tickets = int(input('Please enter how many tickets would you like to buy: '))
day = str(input('Please enter the day you would like to buy tickets for: '))
if day == 'Saturday' or day == 'Sunday':
    weekend = tickets*20
    if weekend >= 100:
        print(f'You bought a Weekend ticket, and spent ${weekend}, you will receive 10% discount and your final price will be ${weekend-(weekend*0.1)}.')
    else:
         print(f'You bought a Weekend ticket, you will pay ${weekend}.')
elif day == 'Tuesday':
    tuesday = tickets*12
    if tuesday >= 100:
        print(f'You bought a Tuesday ticket, and spent ${tuesday}, you will receive 10% discount and your final price will be ${tuesday-(tuesday*0.1)}.')
    else:
        print(f'You bought a Tuesday ticket, you will pay ${tuesday}.')
else:
    weekday = tickets*17
    if weekday >= 100:
        print(f'You bought a Weekday ticket and spent ${weekday}, you will receive 10% discount and your final price will be ${weekday-(weekday*0.1)}')
    else:
        print(f'You bought a Weekday ticket, you will pay ${weekday*17}')

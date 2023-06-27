tickets = int(input('Please enter the number of tickets you would like to buy: '))
day = str(input('Please enter the day of the week that you would to buy tickets for: '))

if day == 'saturday' or day == 'Saturday' or day == 'sunday' or day == 'Sunday':
    weekend = 20*tickets
    if weekend > 100:
        print(f'You spent ${weekend-100} over $100, with 10% discount you will pay ${weekend-weekend*0.1:.2f}')
    else:
        print(f'You bought a Weekend ticket, you will pay ${weekend:.2f}')
elif day == 'Tuesday' or day == 'tuesday':
    tuesday = 12*tickets
    if tuesday > 100:
        print(f'You spent ${tuesday-100} over $100, with 10% discount you will pay ${tuesday-tuesday*0.1:.2f}')
    else:
        print(f'You bought a Tuesday ticket, you will pay ${tuesday:.2f}')
else:
    weekday = 17*tickets
    if weekday > 100:
        print(f'You spent ${weekday-100} over $100, with 10% discount you will pay ${weekday-weekday*0.1:.2f}')
    else:
        print(f'You bought a Weekday ticket, you will pay ${weekday:.2f}')

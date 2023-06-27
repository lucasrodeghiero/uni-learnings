import datetime
day = int(input('Please input day: '))
month = int(input('Please input month: '))
year = int(input('Please input year: '))
date = datetime.date(year,month,day)
print('{:%d-%m-%Y}'.format(date))

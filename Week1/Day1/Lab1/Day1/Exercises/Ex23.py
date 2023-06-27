"""age
100 - age = number of years till 100

then add 2022 to that (100 -age)
"""

name = input('Please enter your name: ')
age = int(input('Please enter you actual age: '))
finalAge = float(100 - age)
print(f'You will turn 100 years old in {finalAge + 2022}')

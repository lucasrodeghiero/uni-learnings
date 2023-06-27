name1,age1 = input('Please enter your name and age: ').split()
name2,age2 = input('Please enter your name and age: ').split()

if age1 > age2:
    print(f'Person {name1} is older! The person is {age1} years old.')
elif age2 > age1:
    print(f' {name2} is older! He is {age2} years old.')
elif age1 == age2:
    print(f'{name1} and {name2} are the same age!.')


#Upper and lower limits
lower = 1
upper = 100

#validation
while(True):
    try:
        num = int(input('Please input a number between 1 and 100: '))
    except ValueError:
        print("Oops! That was not a valid a valid number. Try again...")
    else:
        if 0 <= num <= 100: #check the right range
            break
        else:
            print('Value must be between zero and hundred inclusive')
#compare with lower and upper limits
if num == upper:
    print('Upper limit!')
elif num == lower:
    print('Lower limit')
else:
    print('In range')

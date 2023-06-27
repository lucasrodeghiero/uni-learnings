"""grade1 = float(input('Please enter your first grade: '))
grade2 = float(input('Please enter your second grade: '))
if grade1 > 100:
    print('Invalid grade1, please re-enter.')
    grade1 = float(input('Please enter your first grade: '))
"""
while(True):
    grade1 = int(input('Please enter your first grade: '))
    grade2 = int(input('Please enter your second grade: '))
#LIMITING NUMBER OF ENTRIES
    if grade1 > 100:
        print('Enter a valid number from 1 to 100 to enter you grade!')
    elif grade2 > 100:
        print('Enter a valid number from 1 to 100 to enter you grade!')
    else:
        break
average = (grade1+grade2)/2

if 80 <= average <= 100:
    grade = 'HD'
elif 70 <= average < 80:
    grade = 'D'
elif 60 <= average < 70:
    grade = 'C'
elif 50 <= average < 60:
    grade = 'P'
else:
    grade = 'F'
print(f'Your average: {average: .2f} and Grade = {grade}')

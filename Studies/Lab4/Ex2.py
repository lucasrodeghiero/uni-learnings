"""
Lucas do Amaral
04/03/2022
Reads input from the user, and creates a list accordingly
"""


#use w to write, a to append, r to read
file = open("../student.txt", 'a')

#read inputs from the user
stName = input('Please enter your full name: '+'\n')
stCourse = input('Please enter your course code: '+'\n')
stFee = float(input('Please enter your course fee (single semester) $'))
stDurat = int(input('How many years is your course duration? '))

#Calculate total fee for duration - 2 semester per year
totFee = 2 * stDurat * stFee

#Write text to file
file.write(f'{stName:<10}{stCourse:>10}{totFee:>15.2f}\n')

#Close file after writing
file.close()

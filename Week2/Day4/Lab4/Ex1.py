"""docString..."""
f = open("addExercises/student.txt", "a")

#read inputs
stName = input('Please enter your full name: '+'\n')
stCourse = input('Please enter your course code: '+'\n')
stFee = float(input('Please enter your course fee (single semester) $'))
stDurat = int(input('How many years is your course duration? '))

#calculate total fee for duration - 2 semester per year
totFee = 2 * stDurat * stFee
#write text to file
f.write(f'{stName:<10}{stCourse:>10}{totFee:>15.2f}\n')
#close file after writing
f.close()

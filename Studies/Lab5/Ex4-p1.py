print('\033[1m' + 'This program adds student details to a dictionary' + '\033[0m')
print('------------------------------------------------')

numOfStuds = int(input("How many students: "))
marks = {} #my dictionary, USE CURLY BRACES

for x in range(numOfStuds):
    stID = input('Student ID: ')
    stTot = int(input('Student total mark: '))
    marks[stID] = stTot # adding KEY (stID) and VALUE (stTot) to my blank dictionary

print(f'Marks dictionary: {marks} ')

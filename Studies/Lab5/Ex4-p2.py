file = open('studData.txt', 'a') # append, updating my file every time I enter data

print('\033[1m' + 'This program adds student details to a dictionary' + '\033[0m')
print('------------------------------------------------')

numOfStuds = int(input("How many students: "))
marks = {} #my dictionary, USE CURLY BRACES

for x in range(numOfStuds):
    stID = input('Student ID: ')
    stTot = int(input('Student total mark: '))
    marks[stID] = stTot # adding KEY (stID) and VALUE (stTot) to my blank dictionary
    file.write(f'{stID},{stTot}\n') #writing my inputs into my file

print(f'Marks dictionary: {marks} ')

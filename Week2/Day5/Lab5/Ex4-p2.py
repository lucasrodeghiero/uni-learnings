f = open('studData.txt', 'a')

print( '\033[1m' + 'This program adds student details to a dictionary' + '\033[0m')
print('-------------------------------------------------')

numOfStuds = int(input("How many students: "))
marks = {}
for x in range(numOfStuds):
    stID = input('Student ID: ')
    stTot = int(input('Student total mark: '))
    marks[stID] = stTot
    f.write(f'{stID},{stTot}\n')
f.close()
#print(f'Marks dictionary: {marks}')

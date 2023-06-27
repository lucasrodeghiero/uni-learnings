f = open('studData.txt', 'r')

print( '\033[1m' + 'This program adds student details to a dictionary' + '\033[0m')
print('-------------------------------------------------')

marks = {}

for line in f:
    info = line.split(',')
    marks[info[0]] = int(info[1])
f.close()
print(marks)

f = open('studData.txt', 'r')

print( '\033[1m' + 'This program adds student details to a dictionary' + '\033[0m')
print('-------------------------------------------------')

marks = {} #empty dictionary

for line in f:
    info = line.split(',') #splits the words in each comma
    marks[info[0]] = int(info[1]) #adding data to my dictionary where info[0] stands for KEY and info[1] stands for VALUE
f.close()
print(marks)

f = open('addExercises/para1.txt', 'r')

for line in f:
    if line.startswith('The') or line.startswith('You') or line.startswith('Please'):
        print(line.upper())
    else:
        if line.endswith('unit\n') or line.endswith('document\n'):
            print(line.lower())

f.close()

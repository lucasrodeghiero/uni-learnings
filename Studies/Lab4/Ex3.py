file = open('para1.txt', 'r')

for line in file:
    if line.startswith('The') or line.startswith('You') or line.startswith('Please'):
        print(line.upper())
    else:
        if line.endswith('unit\n') or line.endswith('document\n'):
            print(line.lower())

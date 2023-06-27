file = open('example.txt', 'r')

allWords = file.read().split()

newList = []

for word in allWords:
    lowWd = word.lower()
    if lowWd not in('a', 'an', 'the') and word not in newList:
        newList.append(word)


newList.sort()

print(newList)

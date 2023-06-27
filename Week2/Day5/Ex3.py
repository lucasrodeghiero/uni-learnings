fileName = input('Please enter the file name (eg. myFile.txt): '+' \n')
print('\n')
f = open(fileName, 'r')

# Read the file and split to form a list of words
allWords = (f.read().split())

#Create an empty list 'newList' to hold words that are not articles
newList = []


# Go through all the words in the list
for word in allWords:
    lowWd = word.lower() #convert to lower to match with lowercase of articles
    # Remove any words that are articles or any repeating words
    if lowWd not in ('a', 'an', 'the') and word not in newList:
        newList.append(word)

#Sort the list
newList.sort()

# Print the list with all words
print(newList)

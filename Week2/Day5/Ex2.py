# read a sentence
element = (input('Please input a statement: ').upper())

#produce a list by splitting
words = element.split()

#introduce a new list words1 to add the words
words1 = []

#check each word to if they are an article. If not just add them to the new list.
# else, convert to lowercase and add to the new list.
for word in words:
    if word not in ('A', 'AN', 'THE'):
        words1.append(word)
    else:
        words1.append(word.lower())

#convert to a tuple and print
print(tuple(words1))




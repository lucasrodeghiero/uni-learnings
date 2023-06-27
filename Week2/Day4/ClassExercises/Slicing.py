myString = 'The cat sat on the mat!'
# a) length
print(len(myString))
# b) display the first letter ('T')
print(myString[0])
# c) display the last letter
print(myString[22])
# d) first five characters
print(myString[0:6])
# e) display 4 times
for count in range(4):
    print(myString)
# f) display sub-string
print(myString.find('on'))
print(myString[12:])

print(myString[myString.find('on'):])
# g) list with elements
words = myString.split()
print(words)
# h) all lower case
print(myString.lower())

# i) print sub-string upper case
print(myString.upper()[12:])

# j) check if entire string is alphabetical
print(myString.isalpha())
# k) check if string ends with '!'
print(myString.endswith('!'))
# l) join the letters 'a' 'w' 'e' 's' 'o' 'm' 'e'
letters = ['A', 'w', 'e', 's', 'o', 'm', 'e']
print(''.join(letters))

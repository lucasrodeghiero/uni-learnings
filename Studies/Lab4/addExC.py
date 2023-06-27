words = input('Please enter the word to count: ')

file = open('para.txt', 'r')
read_data = file.read().split()
word_count = read_data.count(words)
print(f'{word_count}')

"""
word = input('Enter the word to count: ')


f = open('para.txt', 'r')
count = 0
for line in f:
     if word in line:
         count = count + 1
print(count)
"""

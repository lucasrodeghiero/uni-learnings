#Request user to input his name
name = str(input('Please enter your name:\n '))
#Request user to input his favourite author
author = str(input(f'Hi {name}, who is your favourite author?\n '))
#Request user to input how many books were read
books = int(input(f'How many books have you read written by {author}?\n '))
print(f'Great {name}, I hope you enjoyed the {books} books you read written by {author}!')

import random

guessesTaken = 0

myName = input("Hello! What's your name? ")
number = random.randint(1,20)
print(f'Well, {myName}, I am thinking of a number between 1 and 20.')

guess = 0
while guessesTaken < 6:
    print('Take a guess:')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print(f'Good job {myName}! You guessed my number in {guessesTaken} guesses!')
if guess != number:
    number = str(number)
    print(f'Nope, The number I was thinking of was {number}')

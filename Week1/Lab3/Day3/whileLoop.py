psWord = input("Please enter your pasword: ")
attempt = 1
while psWord != "koala":
    print("Sorry, wrong password")
    if attempt < 5:
        psWord = input("Please enter your password: ")
        attempt += 1
    else:
        break
if psWord == 'koala':
    print("Welcome! You have logged in successfully!")
else:
    print("No more attempts left! Please try some other time!!")
'''
x = 0
while x < 5:
    print(x)
    x +=1
'''

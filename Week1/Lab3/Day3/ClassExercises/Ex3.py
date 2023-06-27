psWord = input("Please enter your password: ")
attempt = 1
for count in range(3):
    if psWord != "koala":
        print("Sorry wrong password!")
        if attempt <3: #You still have more attempts to go
            psWord = input("Please enter your password: ")
            attempt +=1
        else:
            break #You have used all 3 attempts and breaking the loop
if psWord == 'koala':
    print("Welcome! You have logged in successfully!")
else:
    print("No more attempts left! Please try some other time!")

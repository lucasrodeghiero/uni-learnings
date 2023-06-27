def checkDigits(pswd):
    count = 0
    for let in pswd:
        if let.isdigit():
            count += 1
    return count

def checkUpper(pswd):
    count = 0
    for let in pswd:
        if let.isupper():
            count += 1
    return count

def main():
    print('A valid password must have at least 8 characters, \nwhere one or more should be UPPER case letters.' + '\n' + 'There should be at least one digit.')
    while True:
        password = input('Please enter a password for validation: ' + '\n')
        if len(password) >= 8 and checkUpper(password) >= 1 and checkDigits(password) >= 2:
            print('Password successful!')
            break
        else:
            print('Invalid password!')
main()

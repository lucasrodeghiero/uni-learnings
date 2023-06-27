import re #required package to check special characters

def checkSpecial(pswd):
    regex = re.compile('[@&#%^]')
    if regex.search(pswd) == None:
        return pswd
    else:
        print('Your password contains Special Characters')
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
        if len(password) == 8 and checkUpper(password) >= 3 and checkDigits(password) >= 2 and checkSpecial(password):
            print('Password successful!')
            break
        else:
            print('Invalid password!')
main()

cCode = input('Please enter course code for testing: ')

courseIdent = cCode[0:3]
unitIdent = cCode[3:7]


if len(cCode) != 7:
    print(f'{cCode} is not a valid code. Should be 7 characters long.')
if courseIdent.isalpha() and unitIdent.isdigit():
    print(f'{cCode.upper()} is a valid course code!')
if courseIdent.isalpha() is False or unitIdent.isdigit() is False:
    print(f'{cCode} is not a valid code. Course identifier invalid!')

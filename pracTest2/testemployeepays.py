"""
Lucas do Amaral Martins
14/03/2022
Practical Test 2 - Introduction to Programming
"""

from employeepays import EmployeePays


def main():
    print('------- Beach View Cafe - Employee Pays Progam -------')
    myName = input('Employee name required: ')
    myDate = input('Pay Date (dd/mm/yyyy): ')
    myRole = input('Employee Role - Front Line (FL), Cook (CK), Kitchen Hand (KH): ').upper()

    while True:
        try:
            myHours = int(input('Number hours worked this week: '))
        except ValueError:
            print("A valid input is required for hours!")
        else:
            if 1 <= myHours <= 60:
                break
            else:
                print("Number of work hours must be between 1 - 60")

    myPay = EmployeePays(myName, myDate, myRole, myHours)
    print(myPay)


main()

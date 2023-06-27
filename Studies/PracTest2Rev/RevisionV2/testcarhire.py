from carhire import CarHire

def main():
    print('-------------LUXCARS LUXURY CAR HIRE-------------\n\n')
    myName = input('Please input client name: ')
    myDate = input('Please input hire date: ')
    myCarType = input('Hire cost depends on the type of luxury sports car\n'
                      'FE - (Ferrari), LA - (Lamborghini), MA - (Maserati)\n'
                      'Please select your care type: ').upper()
    while True:
        try:
            myPeriod = int(input('Hire Period (Hours): '))
        except ValueError:
            print("Please enter a valid number for hours required!")
        else:
            if 1 <= myPeriod <= 24:
                break
            else:
                print("Car is rentable for maximum of 24 hours!")
    while True:
        try:
            myNumber = int(input('Number of cars required: '))
        except ValueError:
            print("Please enter a valid number for cars required!")
        else:
            if 1 <= myNumber <= 5:
                break
            else:
                print("Maximum of cars is 5!")

    myCarHire = CarHire(myName, myDate, myCarType, myPeriod, myNumber)

    print(myCarHire)

main()

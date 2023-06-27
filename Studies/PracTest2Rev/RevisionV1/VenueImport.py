from venuebookings import VenueBookings


def main():
    myName = input('Please input customer name: ')
    myDate = input('Please input booking date: ')
    print('Booking costs depends on the venue capacity and the booking period\n'
          'S - (50 - 100 guests), M (100 - 200 guests), L - (200 - 300 guests)')
    myCap = input('Please select your venue capacity option: ').upper()
    myHours = float(input('Booking period (hours): '))
    print('*********** Booking Fee Calculations ***********')
    venuebookings = VenueBookings(myName, myDate, myCap, myHours)

    print(venuebookings)


main()

class VenueBookings(object):
    def __init__(self, name='', date='', capacity='', hours=0):
        self._name = name
        self._date = date
        self._capacity = capacity
        self._hours = hours

    def setName(self, name):
        self._name = name

    def setDate(self, date):
        self._date = date

    def setCap(self, capacity):
        self._capacity = capacity

    def setHours(self, hours):
        self._hours = hours

    def _getPrice(self):  # methods
        price = 0
        if self._capacity == 'S':
            price = 1400.00
        elif self._capacity == 'M':
            price = 1500.00
        elif self._capacity == 'L':
            price = 1650.00
        return price

    def _getCost(self):
        total = self._getPrice() * self._hours
        return total

    def __str__(self):
        return f'-------------- Gala Functions - Booking System --------------\n'\
               f'Booking fee calculation for {self._name} on {self._date}\n' \
               f'Hourly booking cost ${self._getPrice():.2f}\n' \
               f'Total booking cost = ${self._getCost():.2f} for {self._hours} hours.'

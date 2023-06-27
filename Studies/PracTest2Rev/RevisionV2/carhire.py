class CarHire(object):
    def __init__(self, name='', date='', cartype='', period=0, number=0):
        self._name = name
        self._date = date
        self._cartype = cartype
        self._period = period
        self._number = number

    def setName(self, name):
        self._name = name

    def setDate(self, date):
        self._date = date

    def setCarType(self, cartype):
        self._cartype = cartype

    def setPeriod(self, period):
        self._period = period

    def setNumber(self,number):
        self._number = number

    def _getPrice(self):  # methods
        price = 0
        if self._cartype == 'FE':
            price = 650.00
        if self._cartype == 'LA':
            price = 550.00
        if self._cartype == 'MA':
            price = 450.00
        return price

    def _getCost(self):
        total = self._getPrice() * self._period * self._number
        return total

    def __str__(self):
        return f'*************Car Hire Cost Calculations*************\n' \
               f'Car hir calculation for {self._name} on {self._date}\n' \
               f'Hourly hire rate ${self._getPrice():.2f}\n' \
               f'Total hire cost = ${self._getCost():.2f} for {self._number} cars for {self._period} hours.'


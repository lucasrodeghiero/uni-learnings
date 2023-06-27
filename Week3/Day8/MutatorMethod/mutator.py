class Mutator(object):
    def __init__(self, name="", size="", number=0):
        self._name = name
        self._size = size
        self._number = number

    # Mutator Methods
    def setName(self, name):
        self._name = name

    def setSize(self, size):
        self._size = size

    def setNumber(self, number):
        self._number = number

    def _getPrice(self):  # methods
        price = 0
        if self._size == 'small' or self._size == 's':
            price = 8.00
        if self._size == 'medium' or self._size == 'm':
            price = 10.00
        if self._size == 'large' or self._size == 'l':
            price = 12.00
        return price

    def _getTotalCost(self):  # methods
        total = 0
        total = self._getPrice() * self._number
        return total

    def __str__(self):
        return f'Name: {self._name.upper()}\nPizza Size: {self._size.upper()}\nNumber of Pizzas: {self._number}\nPrice of a pizza: ${self._getPrice():0.2f}\nTotal Order Cost: ${self._getTotalCost():0.2f}'

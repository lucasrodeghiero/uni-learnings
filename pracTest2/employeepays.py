"""
Lucas do Amaral Martins
14/03/2022
Practical Test 2 - Introduction to Programming
"""


class EmployeePays(object):
    def __init__(self, name='', date='', role='', hours=0): # Constructor
        self._name = name
        self._date = date
        self._role = role
        self._hours = hours

    # Mutator
    def setName(self, name):
        return name

    def setDate(self, date):
        return date

    def setRole(self, role):
        return role

    def setHours(self, hours):
        return hours

    def _getRate(self): # Accessor
        rate = 0
        if self._role == 'FL':
            rate = 26.50
        if self._role == 'CK':
            rate = 29.50
        if self._role == 'KH':
            rate = 21.50
        return rate

    def _getSalary(self): # Calculating Salary
        salary = self._getRate() * self._hours
        return salary

    def __str__(self): # Output
        return f'\n----------- Employee Pay Slip -----------\n' \
               f'Employee Name: {self._name}\n' \
               f'Date Paid: {self._date}\n' \
               f'Employee Role: {self._role}\n' \
               f'Hourly Rate: ${self._getRate():.2f}\n' \
               f'Number of Hours worked this week: {self._hours:.2f}\n' \
               f'Total Pay earned for this week: ${self._getSalary():.2f}'

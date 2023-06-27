class Student(object):
    def __init__(self, id, name, age, number):
        self._id = id
        self._name = name
        self._age = age
        self._marks = [] # List to hold marks
        for count in range(number):
            self._marks.append(0)

    def _getId(self): # Return the student's id.
        return self._id

    def _getName(self): # Return the student's name.
        return self._name

    def _getAge(self): # Return the student's age.
        return self._age

    def setMark(self, i, score):
        self._marks[i - 1] = score
    def getMark(self,marks):
        return self._marks[] = marks

        # There are 2 under scores before and after str
        # Returns the string representation of the student

    def __str__(self):
        return f'ID: {self._id}\nName: {self._name}\nAge: {self._age}\n{self._marks}'

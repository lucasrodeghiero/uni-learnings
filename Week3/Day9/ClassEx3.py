"""
The two big advantages that these variables have are:

You can associate one variable with more than one widget, so that two or more widgets display exactly the same information all the time
You can bind functions to be called when the values change.

"""

from tkinter import *
import math


class TicketPriceCalc(Frame):
    def __init__(self):
        # Sets up the window and widgets.
        Frame.__init__(self)
        self.master.title("Welcome to Ticket Price Calculator!")
        self.grid()

        # Label and field for the number of tickets
        self._numLabel = Label(self, text="Number of Tickets")
        self._numLabel.grid(row=0, column=0, sticky=W, pady=15)
        self._numVar = IntVar()
        self._numEntry = Entry(self, width=7, textvariable=self._numVar)
        self._numEntry.grid(row=0, column=1)

        # Labels to display total ticket cost
        self._nameLabel = Label(self, text='Calculated ticket cost is: ')
        self._nameLabel.grid(row=4, column=0)
        self._totalVar = DoubleVar()
        self._totLabel = Label(self, textvariable=self._totalVar)
        self._totLabel.grid(row=4, column=1)

        # Create 3 radio buttons
        self._var = DoubleVar()
        self._btn1 = Radiobutton(self, text="Tuesday", variable=self._var, value=12)
        self._btn2 = Radiobutton(self, text="Weekend", variable=self._var, value=20)
        self._btn3 = Radiobutton(self, text="Weekday other than Tuesday", variable=self._var, value=17.50)

        # Add radio buttons to grid
        self._btn1.grid(row=1, column=0, sticky=W)
        self._btn2.grid(row=2, column=0, sticky=W)
        self._btn3.grid(row=3, column=0, sticky=W)

        # The command button
        self._comBtn = Button(self, text='Compute', command=self._total)
        self._comBtn.grid(row=5, column=0)

    def _total(self):
        # Command method for the button
        total = self._var.get() * self._numVar.get()
        self._totalVar.set(f'${total:.2f}')


def main():
    # To instantiate and pop up the window
    TicketPriceCalc().mainloop()


main()

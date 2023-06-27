from tkinter import *

class Greet(Frame): # Class inherits from Frame class
    def __init__(self): # Constructor
        Frame.__init__(self)
        self.master.title("Button & Entry Demo")
        self.grid()
        # Create a label and add to grid
        self._myLabel = Label(self, text='Please enter your name: ') #Instance Variable, Display Message for the User
        self._myLabel.grid(row=0, column=0) #Adding to the grid
        # Create an entry field with a StringVar and add to grid
        self._nameVar = StringVar()
        self._myEnt = Entry(self, textvariable=self._nameVar) #Instance Variable, User Inputs his name
        self._myEnt.grid(row=0, column=1) #Adding to the grid
        # Create a button and add to grid
        self._disButton = Button(self, text='Show Message', command=self._dispGreet) #Instance Variable, Button to be clicked
        self._disButton.grid(row=1, column=0, columnspan=2) #Adding to the grid
        # Create a label to display the greeting and add to grid
        self.greetLab = Label(self, text='') #Instance Variable, Displays message from function _dispGreet + msg
        self.greetLab.grid(row=2, column=0, columnspan=2) #Adding to the grid

    def _dispGreet(self):
        msg = f'Hello, {self._nameVar.get()}! How are you?' # Recalls info from input in line 13
        self.greetLab['text'] = msg

# Instantiate and pop up the window
def main():
    Greet().mainloop()

main()

from tkinter import *

myWindow = Tk()     # Global variable

# Create string variable nameVar for the Entry widget
# Global variable
nameVar = StringVar()
greetVar = StringVar()

def displayGreet():
    greet = (f'Hello, {nameVar.get()}. How are you?')
    greetVar.set(greet)
    
def main():
    myWindow.title("Button & Entry Demo")    # Add a title to myWindow

    myLabel = Label(myWindow, text="Please enter your name: ",fg='green', bg='#00ff99')    # Add a label
    myLabel.grid(row=0, column=0)   # Add the label to the window grid

    #Create an entry field and add to grid
    myEntry = Entry(myWindow, textvariable = nameVar)
    myEntry.grid(row=0, column=1) # Add to grid

    #Create a button and add a method displayGreet() as its command
    disButton = Button(myWindow, text='Submit', command= displayGreet)
    disButton.grid(row=1, column=0, columnspan=2)

    greetLabel = Label(myWindow, textvariable=greetVar)
    greetLabel.grid(row=3, columnspan=2, column= 0)

    myWindow.mainloop()    # Calls the endless loop of the window


main()

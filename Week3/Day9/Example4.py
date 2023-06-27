from tkinter import *

myWindow = Tk() # Create a window called myWindow

def main():
    myWindow.title("Entry Field Demo")    # Add a title to myWindow
    myLabel = Label(myWindow, text="Please enter your name: ",fg='green', bg='#00ff99')    # Add a label
    myLabel.grid(row=0, column=0) # Add the label to the window grid

    #Create an entry field and add to grid
    myEntry = Entry(myWindow)
    myEntry.grid(row=0, column=1)
    myWindow.mainloop()    # Calls the endless loop of the window


main()

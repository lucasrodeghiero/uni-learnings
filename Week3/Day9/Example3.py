from tkinter import *

# Create a window called myWindow
myWindow = Tk()

def main():
    # Add a title to myWindow
    myWindow.title("My Label")

    # Add a label
    myLabel = Label(myWindow, text="Hello World!",fg='green', bg='#00ff99')
    # Add the label to the window grid
    myLabel.grid()

    # Calls the endless loop of the window
    myWindow.mainloop()

main()

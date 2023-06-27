from tkinter import *

# Create a window called myWindow
myWindow = Tk()

# Add a title to myWindow
myWindow.title("My Label")

# Add a label
myLabel = Label(myWindow, text="Hello World!")
# Add the label to the window grid
myLabel.grid()

# Calls the endless loop of the window
myWindow.mainloop()

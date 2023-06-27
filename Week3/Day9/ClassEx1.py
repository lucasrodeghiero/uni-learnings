from tkinter import *

myWindow = Tk()  # Create as global variable

colVar = StringVar(value='Red')  # Create integer variable var for the Entry widget


def sel():
    col = colVar.get()
    print("You selected " + col)


def main():
    myWindow.title("Radio Button Demo")
    # Create an entry field and add to grid
    btn_1 = Radiobutton(myWindow, text='Red', variable=colVar, value='Red', command=sel)
    btn_2 = Radiobutton(myWindow, text='Blue', variable=colVar, value='Blue', command=sel)
    btn_3 = Radiobutton(myWindow, text='Green', variable=colVar, value='Green', command=sel)

    # Add radio buttons to grid
    btn_1.grid(sticky=W)
    btn_2.grid(sticky=W)
    btn_3.grid(sticky=W)

    myWindow.mainloop()  # Calls the endless loop of the window


main()

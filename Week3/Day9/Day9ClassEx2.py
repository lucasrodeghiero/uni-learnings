from tkinter import *


class SimpleGUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("A simple GUI")
        self.grid()

        self._mylabel = Label(self, text="This is a simple GUI application!")
        self._mylabel.grid(row=0, column=0, columnspan=2)
        self._greetbtn = Button(self, text="Greet", command=self._greet)
        self._greetbtn.grid(row=1, column=0)

        self._closebtn = Button(self, text="Close", command=self.quit)
        self._closebtn.grid(row=1, column=1)

    def _greet(self):
        print("Greetings!")


def main():
    SimpleGUI().mainloop()


main()

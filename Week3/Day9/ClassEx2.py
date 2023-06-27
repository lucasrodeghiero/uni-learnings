from tkinter import *


# root = Tk()

class SimpleGUI(Frame):  # Class Constructor
    def __init__(self):
        Frame.__init__(self)
        self.master.title("A simple GUI")  # Window Title
        self.grid()

        self._myLabel = Label(self, text='This is a simple GUI application', fg='light blue', bg='#000000')
        self._myLabel.grid(row=0, columnspan=2, column=0)

        self._greetBtn = Button(self, text='Greet', command=self._greet)
        self._greetBtn.grid(row=1, column=0)

        self.closeBtn = Button(self, text='Quit', command=self.quit)
        self.closeBtn.grid(row=1, column=1)

        self.greetLab = Label(self, text='')  # Instance Variable, Displays message from function _dispGreet + msg
        self.greetLab.grid(row=2, column=0, columnspan=2)  # Adding to the grid

    def _greet(self):
        msg = f'Greetings'  # Recalls info from input in line 13
        self.greetLab['text'] = msg

    # def _quit(self):
    #    root.destroy()


def main():
    SimpleGUI().mainloop()


main()

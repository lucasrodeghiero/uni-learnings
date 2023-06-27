from tkinter import *


class TempConv(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid()
        self._fahrVar = DoubleVar()
        self._celsiusVar = DoubleVar()
        self._fahrVar.set(32.0)
        self._celsiusVar.set(0.0)

        # Labels
        self._fahrLabel = Label(self, text='Fahrenheit', pady=10)
        self._fahrLabel.grid(row=0, column=0)
        self._celsiusLabel = Label(self, text='Celsius', pady=10)
        self._celsiusLabel.grid(row=0, column=1)

        # Entries
        self._fahrEntry = Entry(self, width=15, textvariable=self._fahrVar)
        self._fahrEntry.grid(row=1, column=0)
        self._celsiusEntry = Entry(self, width=15, textvariable=self._celsiusVar)
        self._celsiusEntry.grid(row=1, column=1)

        # Buttons
        self._fahrToCelsBtn = Button(self, text='>>>>',
                                     command=self._toCelsius)
        self._fahrToCelsBtn.grid(row=2, column=0)
        self._celsToFarBtn = Button(self, text='<<<<',
                                    command=self._toFar)
        self._celsToFarBtn.grid(row=2, column=1)

    # Calculate
    def _toCelsius(self):
        fahr = self._fahrVar.get()
        celsius = (fahr - 32) * 5 / 9
        self._celsiusVar.set(celsius)

    def _toFar(self):
        cel = self._celsiusVar.get()
        fahrenheit = cel * 9 / 5 + 32
        self._fahrVar.set(fahrenheit)


def main():
    TempConv().mainloop()


main()

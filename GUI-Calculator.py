
from tkinter import *

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")

        master.config(bg="#0F172A")
        master.resizable(False, False)


        self.equation = StringVar()
        self.entry_value = ""

#############===========================================================================================================

        entry = Entry(master, width=16, bg="gray80", font=("arial bold", 28), textvariable=self.equation,justify="right",border=5)
        entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5,sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),("⌫",1,3) ,
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 1), (".", 5, 1), ("=", 5, 2), ("+", 4, 3),
            ("C", 5, 3),("(",4,0),(")",4,2),("÷", 5, 0)
        ]

##################======================================================================================================
        for (text, row, col) in buttons:
            if text == "=":
                command = self.solve
            elif text == "C":
                command = self.clear

            elif text=="⌫":
                command=self.backspace

            elif text == "x":
                command = lambda: self.show("*")  # internally use *
            elif text == "÷":
                command = lambda: self.show("/")

            else:
                command = lambda t=text: self.show(t)

            button = Button(master, text=text, width=5, height=2, bg="gray30",fg="white",border=3,font=("Arial", 14), command=command,)
            button.grid(row=row, column=col, padx=5, pady=5,sticky="nsew")

#######################+================================================================================================
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

    def backspace(self):

        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)


###############=========================================================================================================
root = Tk()
calculator = Calculator(root)
root.mainloop()


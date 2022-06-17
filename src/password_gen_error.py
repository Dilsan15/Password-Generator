import tkinter as tk


class errorHandle(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()

    @staticmethod
    def error_invalid_entry(entryInput, dropDownInput):
        if any(l.isalpha() for l in entryInput) or any(not c.isalnum() for c in entryInput):
            return False, "Please enter in an integer between 7 - 40"

        elif dropDownInput == "" or entryInput == "":
            return False, "Please fill out the entry AND the dropdown menu"

        elif int(entryInput) > 40 or len(entryInput) >= 3:
            return False, "Input is to long, please type out a number between 7 - 40"

        elif int(entryInput) < 7:
            return False, "Input is to small, please type out a two digit number 7 - 40"

        else:
            return True, 'Success'

# For GUI
import tkinter as tk


class Error_Handle(tk.Tk):
    """checks for errors in user input, initiated by My_Application class. Displays pop-up message if error found"""
    def __init__(self):
        super().__init__()

        # Makes tk not open up a window immediately, as super.init does that
        self.withdraw()

    @staticmethod
    def error_invalid_entry(entry_input, drop_down_input):

        # checks for errors based on input, returns an alert if errors are found in input

        if any(letter.isalpha() for letter in entry_input) or any(not letter.isalnum() for letter in entry_input):
            return False, "Please enter in an integer between 7 - 40"

        elif drop_down_input == "" or entry_input == "":
            return False, "Please fill out the entry AND the dropdown menu"

        elif int(entry_input) > 40 or len(entry_input) >= 3:
            return False, "Input is to long, please type out a number between 7 - 40"

        elif int(entry_input) < 7:
            return False, "Input is to small, please type out a two digit number 7 - 40"

        else:
            return True, 'Success'

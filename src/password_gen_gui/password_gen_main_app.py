# imports needed for GUI
import tkinter as tk
import tkinter.messagebox
import pyglet

# imports for exchanging Data
from src.password_gen_bkend import password_gen_creation
from src.password_gen_gui import password_gen_error


class My_Application(tk.Tk):
    """Is the class responsible for GUI of the application. Takes user input, sends it through processes such as eroor
    checking and password creation, and displays it on the screen."""

    def __init__(self, password_text_gened):
        super().__init__()

        # sets fonts
        pyglet.font.add_file('../assets/fonts/NanumGothicCoding-Bold.ttf')
        pyglet.font.add_file('../assets/fonts/NanumGothicCoding-Bold.ttf')

        # set all variables which will be used in upcoming methods
        self.user_password_gened = password_text_gened
        self.user_password_length = None
        self.user_symbol_selected = None
        self.is_valid_Input = tuple()
        self.error_check = password_gen_error.Error_Handle()

        self.password_length_entry = None
        self.submit_button = None
        self.symbol_drop_down = None

        self.password_heading = None
        self.password_gened_display = None
        self.password_line_display = None

        # run commands to create gui
        self._user_input()
        self._user_output()
        self._run_window()

    def _user_input(self):

        # handle focus func allow for faded out text
        def _handle_focus_in(action):
            self.password_length_entry.delete(0, tk.END)
            self.password_length_entry.config(fg='black')

        def _handle_focus_out(action):
            self.password_length_entry.delete(0, tk.END)
            self.password_length_entry.config(fg='grey')
            self.password_length_entry.insert(0, "Int 7-40")

        # Creates and displays all input boxes, drop-downs and buttons, related to input
        self.user_password_length = tk.StringVar(self)
        self.password_length_entry = tk.Entry(self, textvariable=self.user_password_length,
                                              font=('NanumGothicCoding-Bold', 25), bg="#F2D1D1", fg="grey",
                                              justify="center", width=10)
        self.password_length_entry.pack(side="top", pady=10)

        self.password_length_entry.insert(0, "Int 7-40")

        self.password_length_entry.bind("<FocusIn>", _handle_focus_in)
        self.password_length_entry.bind("<FocusOut>", _handle_focus_out)

        self.user_symbol_selected = tk.StringVar(self)
        self.user_symbol_selected.set("Please Select A Symbol")
        self.symbol_drop_down = tk.OptionMenu(self, self.user_symbol_selected, "%", "#", "^", "*", "\\", "+", "&", "~")
        self.symbol_drop_down.config(bg="#F2D1D1", fg="#231F20", direction="right")
        self.symbol_drop_down.pack(side="top", pady=50)

        self.submit_button = tk.Button(self, font=('NanumGothicCoding-Bold', 20),
                                       command=lambda: self._on_submit(password_length=self.user_password_length.get(),
                                                                       password_symbol=self.user_symbol_selected.get()),
                                       text="Generate", width=15, height=5, bg="#F2D1D1", fg="#231F20")

        self.submit_button.pack()

    def _user_output(self):

        # Creates GUI for displaying user output and copying text
        self.password_heading = tk.Label(self, text="Password:", font=('NanumGothicCoding', 25), bg="#FFE6E6",
                                         fg="#231F20")
        self.password_heading.pack(side="top", pady=50)

        self.password_gened_display = tk.Label(self, text=self.user_password_gened, font=('NanumGothicCoding', 25),
                                               bg="#FFE6E6", fg="#231F20")
        self.password_gened_display.pack(side="top")

        self.password_line_display = tk.Label(self, text="━━━━━━━━━━",
                                              font=('NanumGothicCoding-Bold', 25), bg="#FFE6E6", fg="#231F20")
        self.password_line_display.pack(side="top")

        self.copyToClip = tk.Button(self, text="Copy", bg="#F2D1D1", fg="#231F20", font=('NanumGothicCoding', 20),
                                    command=lambda: [self.clipboard_clear(),
                                                     self.clipboard_append(self.user_password_gened)])
        self.copyToClip.pack(pady=20)

    def _run_window(self):

        # Runs window and adds details such as background color or icon
        self.configure(bg="#FFE6E6")
        self.iconphoto(False, tk.PhotoImage(file="../assets/lockIcon.png"))
        self.title(" Password Generator")
        self.resizable(False, False)
        self.geometry("500x700")
        self.mainloop()

    def _on_submit(self, password_length, password_symbol):

        # Sends data submitted to error checking and password creation methods
        self.clipboard_clear()
        self.is_valid_Input = self.error_check.error_invalid_entry(password_length, password_symbol)

        if self.is_valid_Input[0]:

            passwordHandler = password_gen_creation.Pass_Generator(password_length=password_length,
                                                                   password_symbol=password_symbol)
            passwordHandler.contact_api()
            self.user_password_gened = passwordHandler.password_creator()

        else:
            tk.messagebox.showwarning("Error", self.is_valid_Input[1])
            pass

        # Displaying text on screen
        self.password_gened_display['text'] = self.user_password_gened

        # Adj of font based on user input length
        if len(self.user_password_gened) >= 23:
            self.password_gened_display.config(font=('NanumGothicCoding', 17))

        # Adds password to clipboard based on user choice
        self.clipboard_append(self.user_password_gened)

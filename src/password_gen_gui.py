import time
import tkinter as tk
import tkinter.messagebox

import pyglet

import password_gen_creation
import password_gen_error


class MyApplication(tk.Tk):
    def __init__(self, passwordTextGened):
        super().__init__()

        pyglet.font.add_file('../font_used/nanum_gothic_coding_bold.ttf')
        pyglet.font.add_file('../font_used/nanum_gothic_coding_Regular.ttf')

        self.user_password_gened = passwordTextGened
        self.user_password_length = None
        self.user_symbol_selected = None
        self.is_valid_Input = tuple()
        self.error_check = password_gen_error.errorHandle()

        self.password_length_entry = None
        self.submit_button = None
        self.symbol_drop_down = None

        self.password_heading = None
        self.password_gened_display = None
        self.password_line_display = None

        self._user_input()
        self._user_output()
        self._run_window()

    def _user_input(self):

        def _handleFocusIn(action):
            self.password_length_entry.delete(0, tk.END)
            self.password_length_entry.config(fg='black')

        def _handleFocusOut(action):
            self.password_length_entry.delete(0, tk.END)
            self.password_length_entry.config(fg='grey')
            self.password_length_entry.insert(0, "Int 7-40")

        self.user_password_length = tk.StringVar(self)
        self.password_length_entry = tk.Entry(self, textvariable=self.user_password_length,
                                              font=('NanumGothicCoding-Bold', 25), bg="#F2D1D1", fg="grey",
                                              justify="center", width=10)
        self.password_length_entry.pack(side="top", pady=10)

        self.password_length_entry.insert(0, "Int 7-40")

        self.password_length_entry.bind("<FocusIn>", _handleFocusIn)
        self.password_length_entry.bind("<FocusOut>", _handleFocusOut)

        self.user_symbol_selected = tk.StringVar(self)
        self.user_symbol_selected.set("Please Select A Symbol")
        self.symbol_drop_down = tk.OptionMenu(self, self.user_symbol_selected, "%", "#", "^", "*", "\\", "+", "&", "~")
        self.symbol_drop_down.config(bg="#F2D1D1", fg="#231F20", direction="right")
        self.symbol_drop_down.pack(side="top", pady=50)

        self.submit_button = tk.Button(self, font=('NanumGothicCoding-Bold', 20),
                                       command=lambda: self._on_submit(passwordLength=self.user_password_length.get(),
                                                                       passwordSymbol=self.user_symbol_selected.get()),
                                       text="Generate", width=15, height=5, bg="#F2D1D1", fg="#231F20")

        self.submit_button.pack()

    def _user_output(self):
        self.password_heading = tk.Label(self, text="Password:", font=('NanumGothicCoding', 25), bg="#FFE6E6",
                                         fg="#231F20")
        self.password_heading.pack(side="top", pady=50)

        self.password_gened_display = tk.Label(self, text=self.user_password_gened, font=('NanumGothicCoding', 25),
                                               bg="#FFE6E6", fg="#231F20")
        self.password_gened_display.pack(side="top")

        self.password_line_display = tk.Label(self, text="??????????????????????????????",
                                              font=('NanumGothicCoding-Bold', 25), bg="#FFE6E6", fg="#231F20")
        self.password_line_display.pack(side="top")

        self.copyToClip = tk.Button(self, text="Copy", bg="#F2D1D1", fg="#231F20", font=('NanumGothicCoding', 20),
                                    command=lambda: [self.clipboard_clear(),
                                                     self.clipboard_append(self.user_password_gened)])
        self.copyToClip.pack(pady=20)

    def _run_window(self):
        self.configure(bg="#FFE6E6")
        self.iconphoto(False, tk.PhotoImage(file="../images_used/tk_password_logo.png"))
        self.title(" Password Generator")
        self.resizable(False, False)
        self.geometry("500x700")
        self.mainloop()

    def _on_submit(self, passwordLength, passwordSymbol):

        self.clipboard_clear()
        self.is_valid_Input = self.error_check.error_invalid_entry(passwordLength, passwordSymbol)

        if self.is_valid_Input[0]:

            passwordHandler = password_gen_creation.passGenerator(passwordLength=passwordLength,
                                                                  passwordSymbol=passwordSymbol)
            passwordHandler.contactAPI()
            self.user_password_gened = passwordHandler.passwordCreater()
            time.sleep(0.25)

        else:
            tk.messagebox.showwarning("Error", self.is_valid_Input[1])
            pass

        self.password_gened_display['text'] = self.user_password_gened

        if len(self.user_password_gened) >= 23:
            self.password_gened_display.config(font=('NanumGothicCoding', 17))

        self.clipboard_append(self.user_password_gened)

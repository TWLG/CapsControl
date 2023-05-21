# CapsControl quick clipboard text manipulator.

import pyperclip
import tkinter as tk


class Display:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.title("CapsControl")

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=2)

        self.clipboard_text = tk.Text(self.root, height=20, width=40)

        self.menu()
        self.root.mainloop()

    def menu(self):
        upper_button = tk.Button(
            self.root,
            text="upper",
            command=self.convert_upper
        )
        upper_button.grid(
            row=0,
            column=1
        )

        lower_button = tk.Button(
            self.root,
            text="lower",
            command=self.convert_lower
        )
        lower_button.grid(
            row=0,
            column=2
        )
        self.clipboard_text.grid(
            columnspan=6,
            row=1,
            column=1
        )
        exit_button = tk.Button(
            self.root,
            text='Exit',
            command=lambda: self.root.quit()
        )
        exit_button.grid(
            row=0,
            column=3
        )

    def convert_upper(self):
        s = pyperclip.paste()
        pyperclip.copy(s.upper())
        print(s.upper())
        self.clipboard_text.delete("1.0", "end")
        self.clipboard_text.insert(tk.END, s)

    def convert_lower(self):
        s = pyperclip.paste()
        pyperclip.copy(s.lower())
        print(s.lower())
        self.clipboard_text.delete("1.0", "end")
        self.clipboard_text.insert(tk.END, s)


display = Display()

# end of file

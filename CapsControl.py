# CapsControl quick clipboard text manipulator.

import pyperclip
import tkinter as tk
import re


class Display:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.title("CapsControl")

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=2)

        self.clipboard_text = tk.Text(self.root, height=10, width=20)
        self.currentSaved = pyperclip.paste()
        self.clipboard_text.insert(tk.END, self.currentSaved)

        self.history = Stack()
        self.lastCommand = None

        self.menu()
        self.root.mainloop()

    def menu(self):
        # Ensure this is not a duplicate command
        # Update the variable to the current function
        if self.lastCommand == "menu":
            return
        self.lastCommand = "menu"

        upper_button = tk.Button(
            self.root,
            text="upper",
            command=self.convert_upper
        )
        upper_button.grid(
            row=0,
            column=0
        )

        lower_button = tk.Button(
            self.root,
            text="lower",
            command=self.convert_lower
        )
        lower_button.grid(
            row=1,
            column=0
        )

        remove_punctuation = tk.Button(
            self.root,
            text="remove_punctuation",
            command=self.remove_punctuation
        )
        remove_punctuation.grid(
            row=0,
            column=2
        )

        remove_non_letters = tk.Button(
            self.root,
            text="remove_non_letters",
            command=self.remove_non_letters
        )
        remove_non_letters.grid(
            row=1,
            column=2
        )

        smash = tk.Button(
            self.root,
            text="smash",
            command=self.smash
        )
        smash.grid(
            row=2,
            column=2
        )

        word_list_view = tk.Button(
            self.root,
            text="word_list_view",
            command=self.word_list_view
        )
        word_list_view.grid(
            row=0,
            column=3
        )

        clean_newlines = tk.Button(
            self.root,
            text="clean",
            command=self.clean_newlines
        )
        clean_newlines.grid(
            row=1,
            column=3
        )

        title_casing = tk.Button(
            self.root,
            text="title_case",
            command=self.title_casing
        )
        title_casing.grid(
            row=2,
            column=3
        )

        undo_button = tk.Button(
            self.root,
            text='undo',
            command=self.undo_last
        )
        undo_button.grid(
            row=1,
            column=5
        )

        exit_button = tk.Button(
            self.root,
            text='Exit',
            command=lambda: self.root.quit()
        )
        exit_button.grid(
            row=2,
            column=5
        )

        self.clipboard_text.grid(
            columnspan=6,
            row=3,
            column=1
        )

    def set_clipboard(self, s):

        pyperclip.copy(s)
        self.clipboard_text.delete("1.0", "end")
        self.clipboard_text.insert(tk.END, s)

    def undo_last(self):

        if self.history.is_empty():
            return

        s = self.history.peek()
        pyperclip.copy(s)
        self.set_clipboard(s)
        self.history.pop()

    def convert_upper(self):
        if self.lastCommand == "convert_upper":
            return
        self.lastCommand = "convert_upper"
        self.history.push(pyperclip.paste())

        s = pyperclip.paste().upper()
        self.set_clipboard(s)

    def convert_lower(self):
        if self.lastCommand == "convert_lower":
            return
        self.lastCommand = "convert_lower"
        self.history.push(pyperclip.paste())

        s = pyperclip.paste().lower()
        self.set_clipboard(s)

    def remove_punctuation(self):
        if self.lastCommand == "remove_punctuation":
            return
        self.lastCommand = "remove_punctuation"
        self.history.push(pyperclip.paste())

        s = re.sub(r'[^\w\s]', ' ', pyperclip.paste())
        self.set_clipboard(s)

    def remove_non_letters(self):
        if self.lastCommand == "remove_non_letters":
            return
        self.lastCommand = "remove_non_letters"
        self.history.push(pyperclip.paste())

        s = re.sub(r'[^a-zA-Z]', ' ', pyperclip.paste())
        self.set_clipboard(s)

    def smash(self):
        if self.lastCommand == "smash":
            return
        self.lastCommand = "smash"
        self.history.push(pyperclip.paste())

        s = re.sub(r'\s', '', pyperclip.paste())
        self.set_clipboard(s)

    def word_list_view(self):
        if self.lastCommand == "word_list_view":
            return
        self.lastCommand = "word_list_view"
        self.history.push(pyperclip.paste())

        s = re.sub(r'\s+', ',\n', pyperclip.paste())
        self.set_clipboard(s)

    def clean_newlines(self):
        if self.lastCommand == "clean_newlines":
            return
        self.lastCommand = "clean_newlines"
        self.history.push(pyperclip.paste())

        s = re.sub(r' +', ' ', re.sub(r'\n+', ' ', pyperclip.paste()))
        self.set_clipboard(s)

    def title_casing(self):
        if self.lastCommand == "title_casing":
            return
        self.lastCommand = "title_casing"
        self.history.push(pyperclip.paste())

        s = pyperclip.paste().title()
        self.set_clipboard(s)


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


display = Display()

# end of file

# CapsControl quick clipboard text manipulator.
import tkinter
import pyperclip

window = tkinter.Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("CapsControl")


window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=2)

clipboard_text = tkinter.Text(window, height=20, width=40)
def convertUpper():
    s = pyperclip.paste()
    pyperclip.copy(s.upper())
    print(s.upper())
    clipboard_text.delete("1.0", "end")
    clipboard_text.insert(tkinter.END, s)

def convertLower():
    s = pyperclip.paste()
    pyperclip.copy(s.lower())
    print(s.lower())
    clipboard_text.delete("1.0", "end")
    clipboard_text.insert(tkinter.END, s)

upper_button = tkinter.Button(
    window,
    text="upper",
    command=convertUpper
)

upper_button.grid(
    row=0,
    column=1
)

lower_button = tkinter.Button(
    window,
    text="lower",
    command=convertLower
)

lower_button.grid(
    row=0,
    column=2
)


clipboard_text.grid(
    columnspan=6,
    row=1,
    column=1
)


exit_button = tkinter.Button(
    window,
    text='Exit',
    command=lambda: window.quit()
)
exit_button.grid(
    row=0,
    column=3
)
def main():
    window.mainloop()

    convertUpper()


main()

# end of file

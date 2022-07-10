from random import *
from tkinter import *
import string

textfield = ""
history = ""
# <editor-fold desc= "[Password Data]">
upper_char = string.ascii_uppercase
uppercase = {index + 1: letter for index, letter in enumerate(upper_char)}

low_char = string.ascii_lowercase
lowercase = {index + 1: letter for index, letter in enumerate(low_char)}

numbers = string.digits
digits = {index + 1: letter for index, letter in enumerate(numbers)}

sign = string.punctuation
signs = {index + 1: letter for index, letter in enumerate(sign)}


# </editor-fold>
def password_generator():
    password = [
        uppercase[randint(1, len(uppercase))],
        uppercase[randint(1, len(uppercase))],
        lowercase[randint(1, len(lowercase))],
        lowercase[randint(1, len(lowercase))],
        lowercase[randint(1, len(lowercase))],
        lowercase[randint(1, len(lowercase))],
        lowercase[randint(1, len(lowercase))],
        lowercase[randint(1, len(lowercase))],
        lowercase[randint(1, len(lowercase))]
    ]

    password_two = [
        digits[randint(1, len(digits))],
        digits[randint(1, len(digits))],
        signs[randint(1, len(signs))],
        signs[randint(1, len(signs))]
    ]
    shuffle(password)
    shuffle(password_two)
    swag = ''.join(password)
    swag_two = ''.join(password_two)
    return swag + swag_two

def clear_history():
    global history
    history = ""
    text_history.delete(1.0, "end")

def add_to_textfield():
    global textfield, history
    textfield = password_generator()
    history +=  f'{textfield}\n'
    text_results.delete(1.0, "end")
    text_results.insert(1.0, textfield)
    text_history.insert(1.0, history)
    history = ""

root = Tk()
root.title("CRPG")
root.geometry("300x650")
root.resizable(0, 0)
text_results = Text(root, height=1, width=len(password_generator()), font=("Arial", 25), borderwidth=1)
text_history = Text(root, height=14, width=len(password_generator())+2, font=("Arial", 20), borderwidth=1)
text_results.grid(row=1, column=1, columnspan=2)
text_history.grid(row=3, column=1, columnspan=3)


# <editor-fold desc= "[Buttons]">
btn = Button(root, text="Generate", command=lambda:add_to_textfield(), width=10, font=("Impact", 14))
btn.grid(row=2, column=1)
btn1 = Button(root, text="Clear", command=lambda:clear_history(), width=10, font=("Impact", 14))
btn1.grid(row=2, column=2)
# </editor-fold>

root.mainloop()
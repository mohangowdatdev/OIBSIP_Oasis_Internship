import random
import string
from tkinter import *
from tkinter import ttk
import pyperclip


# Define functions
def generate_password():
    """Generates a random password based on user input."""
    password_length = int(length_entry.get())
    characters = ""
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_numbers.get():
        characters += string.digits
    if include_symbols.get():
        characters += string.punctuation

    if not characters:
        password_label.config(text="Please select at least one character type.")
        return

    password = "".join(random.choices(characters, k=password_length))
    password_label.config(text=password, font=("Arial", 14, "bold"))
    password_label.grid(row=9, column=0, columnspan=2, sticky=NSEW)


def copy_password():
    """Copies the generated password to the clipboard."""
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        password_label.config(text="Copied to clipboard")


# Initialize the window
root = Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(background="#f0f0f0")

# Add padding
for widget in root.winfo_children():
    widget.grid(padx=10, pady=5)

# Create title label
title_label = Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, sticky=NSEW)


# Length options
length_label = Label(root, text="Length:", font=("Arial", 12))
length_label.grid(row=3, column=0, sticky=W)
length_entry = Entry(root, width=5, font=("Arial", 12))
length_entry.insert(END, 12)
length_entry.grid(row=3, column=1, sticky=W)

# Character type checkboxes
include_uppercase = IntVar(value=1)
include_lowercase = IntVar(value=1)
include_numbers = IntVar(value=1)
include_symbols = IntVar(value=0)

uppercase_checkbox = Checkbutton(
    root, text="Uppercase", variable=include_uppercase, font=("Arial", 12)
)
uppercase_checkbox.grid(row=4, column=0, sticky=W)
lowercase_checkbox = Checkbutton(
    root, text="Lowercase", variable=include_lowercase, font=("Arial", 12)
)
lowercase_checkbox.grid(row=5, column=0, sticky=W)
numbers_checkbox = Checkbutton(
    root, text="Numbers", variable=include_numbers, font=("Arial", 12)
)
numbers_checkbox.grid(row=6, column=0, sticky=W)
symbols_checkbox = Checkbutton(
    root, text="Symbols", variable=include_symbols, font=("Arial", 12)
)
symbols_checkbox.grid(row=7, column=0, sticky=W)

# Buttons
generate_button = Button(
    root, text="Generate", command=generate_password, font=("Arial", 12)
)
generate_button.configure(
    background="#2980b9", foreground="#ffffff", activebackground="#2471a3"
)
generate_button.grid(row=8, column=0, sticky=NSEW)

copy_button = Button(root, text="Copy", command=copy_password, font=("Arial", 12))
copy_button.configure(
    background="#2980b9", foreground="#ffffff", activebackground="#2471a3"
)
copy_button.grid(row=8, column=1, sticky=NSEW)

# Password label
password_label = Label(root, text="", background="#ffffff")
password_label.grid(row=9, column=0, columnspan=2, sticky=NSEW)


# Run the main loop
root.mainloop()

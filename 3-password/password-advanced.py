import tkinter as tk
from tkinter import ttk, messagebox
from zxcvbn import zxcvbn
import pyperclip
import string
import random


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_label = ttk.Label(root, text="Generated Password:")
        self.password_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            root, textvariable=self.password_var, state="readonly", font=("Arial", 12)
        )
        self.password_entry.grid(
            row=1, column=0, columnspan=3, pady=10, padx=10, sticky="ew"
        )

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        self.length_var = tk.IntVar(value=12)
        self.length_entry = ttk.Entry(
            root, textvariable=self.length_var, font=("Arial", 12), width=5
        )
        self.length_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        self.lower_var = tk.IntVar(value=1)
        self.lower_check = ttk.Checkbutton(
            root, text="Include Lowercase", variable=self.lower_var
        )
        self.lower_check.grid(
            row=3, column=0, columnspan=2, pady=5, padx=10, sticky="w"
        )

        self.upper_var = tk.IntVar(value=1)
        self.upper_check = ttk.Checkbutton(
            root, text="Include Uppercase", variable=self.upper_var
        )
        self.upper_check.grid(
            row=4, column=0, columnspan=2, pady=5, padx=10, sticky="w"
        )

        self.digit_var = tk.IntVar(value=1)
        self.digit_check = ttk.Checkbutton(
            root, text="Include Numbers", variable=self.digit_var
        )
        self.digit_check.grid(
            row=5, column=0, columnspan=2, pady=5, padx=10, sticky="w"
        )

        self.symbol_var = tk.IntVar(value=1)
        self.symbol_check = ttk.Checkbutton(
            root, text="Include Symbols", variable=self.symbol_var
        )
        self.symbol_check.grid(
            row=6, column=0, columnspan=2, pady=5, padx=10, sticky="w"
        )

        self.generate_button = ttk.Button(
            root, text="Generate Password", command=self.generate_password
        )
        self.generate_button.grid(row=7, column=0, columnspan=3, pady=10)

        self.copy_button = ttk.Button(
            root, text="Copy to Clipboard", command=self.copy_to_clipboard
        )
        self.copy_button.grid(row=8, column=0, columnspan=3, pady=10)

        self.strength_button = ttk.Button(
            root, text="Check Password Strength", command=self.show_strength_page
        )
        self.strength_button.grid(row=9, column=0, columnspan=3, pady=10)

    def generate_password(self):
        chars = ""
        if self.lower_var.get():
            chars += string.ascii_lowercase
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.digit_var.get():
            chars += string.digits
        if self.symbol_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showinfo("Error", "Please select at least one character type.")
            return

        password = "".join(random.choice(chars) for _ in range(self.length_var.get()))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

    def show_strength_page(self):
        strength_page = tk.Toplevel(self.root)
        strength_page.title("Password Strength Checker")

        password_label = ttk.Label(strength_page, text="Enter or Paste Password:")
        password_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        password_var = tk.StringVar()
        password_entry = ttk.Entry(
            strength_page, textvariable=password_var, show="*", font=("Arial", 12)
        )
        password_entry.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        check_button = ttk.Button(
            strength_page,
            text="Check Strength",
            command=lambda: self.check_strength(strength_page, password_var.get()),
        )
        check_button.grid(row=2, column=0, pady=10)

        strength_label = ttk.Label(strength_page, text="", font=("Arial", 12))
        strength_label.grid(row=3, column=0, columnspan=3, pady=10)

        feedback_label = ttk.Label(strength_page, text="", font=("Arial", 12))
        feedback_label.grid(row=4, column=0, columnspan=3, pady=5)

        time_label = ttk.Label(strength_page, text="", font=("Arial", 12))
        time_label.grid(row=5, column=0, columnspan=3, pady=5)

    def check_strength(self, strength_page, password):
        result = zxcvbn(password)
        strength = result["score"]
        feedback = result["feedback"]["suggestions"]
        time_to_crack = result["crack_times_display"][
            "offline_slow_hashing_1e4_per_second"
        ]

        strength_text = ""
        color = ""

        if strength == 0:
            strength_text = "Impossible"
            color = "red"
        elif strength == 1:
            strength_text = "Easy"
            color = "orange"
        elif strength == 2:
            strength_text = "Good"
            color = "yellow"
        elif strength == 3:
            strength_text = "Hard"
            color = "green"
        elif strength == 4:
            strength_text = "Very Hard"
            color = "blue"

        strength_label = ttk.Label(
            strength_page,
            text=f"Strength: {strength_text}",
            font=("Arial", 12),
            foreground=color,
        )
        strength_label.grid(row=3, column=0, columnspan=3, pady=10)

        time_label = ttk.Label(
            strength_page,
            text=f"Estimated time to crack: {time_to_crack}",
            font=("Arial", 12),
        )
        time_label.grid(row=5, column=0, columnspan=3, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

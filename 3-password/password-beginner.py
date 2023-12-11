# Language: Python 3
# Author: Mohan Gowda T { GitHub @ mohangowdatdev }
# Created date: 17-11-2023
# Description: Generating passwords based on user preferences for Oasis Infobyte Internship Program
# Project 3: Password Generator ( Beginner )

import string
import random
from termcolor import colored

print("\n" + "-" * 45)
print("     🔒|- Enigma Password Generator -|🔒")
print("-" * 45 + "\n")

while True:
    # Getting Characters list for passwords
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "="]

    # Password Data Inputs
    plen = int(input(colored("🌟 Password Length: ", "red")))
    charTrue = input(colored("Include Alphabets? (y/n): ", "red"))
    digTrue = input(colored("Include Digits? (y/n): ", "red"))
    symTrue = input(colored("Include Special Characters? (y/n): ", "red"))

    # Creating character list
    characters = []
    if charTrue == "y" or charTrue == "Y":
        characters += letters
    if digTrue == "y" or digTrue == "Y":
        characters += digits
        characters += digits
    if symTrue == "y" or symTrue == "Y":
        characters += special_chars

    # Generating the Password
    password = []
    for i in range(plen):
        password.append(random.choice(characters))

    # Printing the Password
    password = "".join(password)
    print(f"\n🔐 Password : {colored(password,'green')}")
    print("\n" + "=" * 45)

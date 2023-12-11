# Language: Python 3
# Author: Mohan Gowda T { GitHub @ mohangowdatdev }
# Created date: 15-11-2023
# Description: Calculate BMI based on height & weight for Oasis Infobyte Internship Program
# Project 2: BMI Calculator ( Beginner )


# Calculating the BMI
def bmicalci(weight, height):
    bmi = weight / (height**2)
    return bmi


# Checking the Category of the BMI
def category(bmi):
    if bmi < 18.5:
        return "[ Underweight ] - Eat More & Bulk-up!"
    elif 18.5 <= bmi < 25:
        return "[ Normal ] - Good Work There!"
    elif 25 <= bmi < 30:
        return "[ Overweight ] - Grab a Dumbell or Running Shoes!"
    else:
        return "[ Obese ] - Workout More & Eat Healthy!"


# Main Part of the Program
print("=" * 30)
print("     +- BMI Calculator! -+")
print("=" * 30)
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))
bmi = bmicalci(weight, height)
category = category(bmi)

# Printing the Result
print("_" * 30)
print("🌟 BMI Result: {:.2f}".format(bmi))
print("👀 Category: {}".format(category))
print("=" * 30)

# Language: Python 3
# Author: Mohan Gowda T { GitHub @ mohangowdatdev }
# Created date: 03-12-2023
# Description: Building a Voice Assistant for Oasis Infobyte Internship Program
# Project 1: Voice Assistant with Python (Beginner)

# Importing the Libraries
from ctypes import alignment
from math import e
import os
import datetime
import time
import pyttsx3
import speech_recognition as sr
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.text import Text
import pyjokes
import wikipedia
import ecapture as ec


# Initializing the Libraries
engine = pyttsx3.init()
recognizer = sr.Recognizer()
console = Console()

# Changing Rate, Volume and Voice of the Assistant
engine.setProperty("rate", 200)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def initialize_animation(adv):
    # Progress Bar to Initialize the Assistant
    with Progress() as progress:
        initialze_bar = progress.add_task("[cyan]Initializing... ", total=100)
        while not progress.finished:
            progress.update(initialze_bar, advance=adv)
            time.sleep(0.02)
    os.system("cls" if os.name == "nt" else "clear")
    print("/root/TOM/Initialized Successfully !!\n" + "_" * 130)
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
    print("+" + "-" * 128 + "+")
    print("|" + " " * 128 + "|")
    print("|" + " " * 51 + "-> TOM AT YOUR SERVICE <-" + " " * 52 + "|")
    print("|" + " " * 128 + "|")
    print("+" + "-" * 128 + "+")


def speak(message):
    # Print what assistant says on terminal
    console.print(
        Panel(
            Text(message, style="bold green"),
            title="TOM",
            width=130,
            title_align="left",
            padding=(1, 2),
            style="bold green",
        )
    )
    engine.say(message)
    engine.runAndWait()


def user(message):
    # Print what user says on terminal
    console.print(
        Panel(
            Text(message, style="bold blue", justify="right"),
            title="YOU",
            title_align="right",
            width=130,
            padding=(0, 2),
        )
    )


def listen():
    # Listen to user's voice command
    with sr.Microphone() as source:
        console.print("Listening [🎙️]", style="bold green", end="\r")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
        except sr.WaitTimeoutError:
            console.print("\nSorry, Nothing Heard.", style="bold red", end="\r")
            return None

    try:
        console.print("Thinking [🧠]", style="bold blue", end="\r")
        command = recognizer.recognize_google(audio).capitalize()
        return command

    except sr.UnknownValueError:
        console.print(
            "\nSorry, could not understand your voice.", style="bold red", end="\r"
        )
        return None
    except sr.RequestError:
        console.print("\nFailed to Fetch :(", style="bold red", end="\r")
        return None


def main():
    os.system("cls" if os.name == "nt" else "clear")
    initialize_animation(3.0)
    speak("Hello, I am TOM, your personal assistant.")

    while True:
        command = listen()
        if command == None:
            continue
        user(command)
        command = command.lower()

        if "hello" in command or "hi" in command or "hey" in command:
            speak("Hello! How can I assist you today?")

        elif "what can you do" in command:
            speak(
                "I can do many things, for example \n- I can tell you Date and Time\n- Have Casual Conversations\n- Do system operations such as Lock Windows\n- Make a Google and Wikipedia Search \n- Open Google, Youtube, G-Mail and VS Code\n- Tell you a Joke\n- Take a Photo\n- And much more.."
            )

        elif "what is your name" in command or "who are you" in command:
            speak(
                "My name is TOM, your personal assistant. Feel free to ask me anything. I am still learning a lot. Hope I could be of help to you."
            )

        elif "time" in command:
            now = datetime.datetime.now()
            speak(
                "The current time is "
                + str(now.hour)
                + " hours and "
                + str(now.minute)
                + " minutes."
            )

        elif "date" in command:
            now = datetime.datetime.now()
            speak(
                "The current date is "
                + str(now.day)
                + " "
                + str(now.strftime("%B"))
                + " "
                + str(now.year)
                + "."
            )

        elif "open google" in command:
            speak("Opening Google...")
            os.system("start brave https://www.google.com")

        elif "open youtube" in command:
            speak("Opening Youtube...")
            os.system("start brave https://www.youtube.com")

        elif "open gmail" in command:
            speak("Opening G-Mail...")
            os.system("start brave https://www.gmail.com")

        elif "wikipedia" in command:
            speak("Searching Wikipedia...")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            speak("For more information, please visit Wikipedia.")

        elif "open code" in command:
            speak("Opening VS Code...")
            os.startfile(
                "d:/Programming/Python/4_Projects/oasis/1-voiceassist/voice-beginner.py"
            )

        elif "capture" in command or "photo" in command:
            speak("Taking a photo...")
            ec.capture(0, "robo camera", "img.jpg")

        elif "lock" in command:
            speak("Locking the device...")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif (
            "quit" in command
            or "exit" in command
            or "goodbye" in command
            or "bye" in command
        ):
            speak("Goodbye! Have a nice day.")
            break

        elif (
            "thank you" in command
            or "thanks" in command
            or "good job" in command
            or "well done" in command
            or "great" in command
            or "awesome" in command
            or "cool" in command
            or "nice" in command
        ):
            speak("You're welcome. Glad I could be of help.")

        elif "joke" in command:
            speak(pyjokes.get_joke())

        else:
            speak("Sorry, I'm still learning. I don't know that yet.")

    print("TOM Left the Chat !!💨\n" + "_" * 130)


if __name__ == "__main__":
    main()

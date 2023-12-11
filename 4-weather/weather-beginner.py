# Language: Python 3
# Author: Mohan Gowda T { GitHub @ mohangowdatdev }
# Created date: 19-11-2023
# Description: A beginner level weather app using OpenWeatherMap API for Oasis Infobyte Internship Program
# Project 4: Weather App ( Beginner )

import requests
from colorama import init, Fore
from tabulate import tabulate
from termcolor import cprint

init(autoreset=True)  # Reset the colorama module after each print statement


# Fetch the weather data from OpenWeatherMap API using the requests library
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        cprint(
            f"Sorry!! No Weather Data Found. Please check the city name or ZIP code.",
            "red",
        )
        return None


def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_condition = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        pressure = weather_data["main"]["pressure"]

        table = [
            [f"{Fore.GREEN}City:", city],
            [f"{Fore.GREEN}Temperature:", f"{temperature}°C"],
            [f"{Fore.GREEN}Humidity:", f"{humidity}%"],
            [f"{Fore.GREEN}Weather Condition:", weather_condition],
            [f"{Fore.GREEN}Wind Speed:", f"{wind_speed} m/s"],
            [f"{Fore.GREEN}Pressure:", f"{pressure} hPa"],
        ]

        print(tabulate(table, tablefmt="fancy_grid"))


api_key = "c23eeec320ce8520b34cd9abd5320670"  # API Key from OpenWeatherMap
cprint("\n" + "-" * 35, "magenta")
cprint("   ⛅ SnowFlake Weather App ⛅", "green", attrs=["bold", "blink"])
cprint("-" * 35, "magenta")

while True:
    location = input("Enter city or ZIP code: ")
    if location == "exit" or location == "quit":
        print("\nThank you. Have a Shiny Day!!🌞\n" + "-" * 35  +"\n")
        break
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)
    cprint("\n" + "-" * 35, "yellow")

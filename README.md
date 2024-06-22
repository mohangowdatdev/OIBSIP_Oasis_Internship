---

# Voice Assistant, BMI Calculator, Password Generator, and Weather App

This repository contains four beginner-level projects created during an internship at Oasis Infobytes. Each project showcases the use of various Python libraries and tools to create interactive applications. The projects are

1. [Voice Assistant](#voice-assistant)
2. [BMI Calculator](#bmi-calculator)
3. [Password Generator](#password-generator)
4. [Weather App](#weather-app)

## Voice Assistant

### Features
- **Voice Interaction:** Interact with the assistant using voice commands.
- **Text-to-Speech:** The assistant responds with spoken messages.
- **Utility Functions:** Perform tasks like checking the time, date, opening websites, and locking the system.
- **Wikipedia Search:** Get brief summaries from Wikipedia.
- **Jokes:** Get a random joke.
- **Capture Photo:** Take a photo using your webcam.

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohangowdatdev/oasis-infobyte.git
   cd oasis-infobyte
   ```

2. **Install dependencies:**
   ```bash
   pip install pyttsx3 speechrecognition rich pyjokes wikipedia ecapture
   ```

3. **Run the voice assistant:**
   ```bash
   python voice_assistant.py
   ```

## BMI Calculator

### Features
- **Calculate BMI:** Enter weight and height to calculate BMI.
- **BMI History:** Save BMI calculations and view history.
- **BMI Trends:** Analyze BMI trends over time with a graph.

### Installation
1. **Install dependencies:**
   ```bash
   pip install matplotlib
   ```

2. **Run the BMI calculator:**
   ```bash
   python bmi_calculator.py
   ```

### Usage
1. Enter your weight and height.
2. Click on "Calculate BMI" to see the result.
3. Click on "View BMI History" to see past calculations.
4. Click on "Analyze BMI Trends" to see a graph of your BMI over time.

## Password Generator

### Features
- **Generate Passwords:** Create strong passwords with customizable options (length, character types).
- **Copy to Clipboard:** Copy the generated password to the clipboard.
- **Password Strength Checker:** Check the strength of a password.

### Installation
1. **Install dependencies:**
   ```bash
   pip install zxcvbn pyperclip
   ```

2. **Run the password generator:**
   ```bash
   python password_generator.py
   ```

### Usage
1. Set the desired password length.
2. Choose the types of characters to include (lowercase, uppercase, numbers, symbols).
3. Click "Generate Password" to create a password.
4. Click "Copy to Clipboard" to copy the password.
5. Click "Check Password Strength" to evaluate a password's strength.

## Weather App

### Features
- **Fetch Weather Data:** Retrieve current weather data for a specified city or ZIP code.
- **Display Weather Information:** Show detailed weather information including temperature, humidity, weather condition, wind speed, and pressure.

### Installation
1. **Install dependencies:**
   ```bash
   pip install requests colorama tabulate termcolor
   ```

2. **Run the weather app:**
   ```bash
   python weather_app.py
   ```

### Usage
1. Enter the name of a city or a ZIP code to get the weather information.
2. Type "exit" or "quit" to close the application.

### Note
Replace the `api_key` variable in `weather_app.py` with your own API key from [OpenWeatherMap](https://openweathermap.org/api).

---

## Contribution
Feel free to fork this repository and contribute by submitting a pull request.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Author
**Mohan Gowda T**  
GitHub: [mohangowdatdev](https://github.com/mohangowdatdev)

---

This README provides a comprehensive guide to each project, including features, installation instructions, and usage information.

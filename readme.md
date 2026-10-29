# 🌤️ Terminal Weather App

A simple, interactive command-line weather application built with Python. It fetches current weather data for cities around the world using the free [Open-Meteo API](https://open-meteo.com/), with no API key required.

## ✨ Features

- **No API Key Required** — Uses Open-Meteo's free Geocoding and Weather APIs.
- **City Search** — Converts city names into geographic coordinates using the Geocoding API.
- **Live Weather Data** — Retrieves current weather information based on the selected city's coordinates.
- **Error Handling** — Handles invalid inputs and unsuccessful searches without unexpectedly crashing.
- **Retro Terminal Banner** — Displays custom ASCII art when the application starts.

## 🛠️ Built With

- **Python 3** — Core application logic.
- **Requests** — Sends HTTP GET requests to the APIs.
- **JSON** — Processes API responses and extracts relevant weather and location data.
- **Control Flow** — Uses loops and conditional statements to validate input and maintain an interactive experience.

## 📦 Installation

### Prerequisites

- Python 3 installed on your system.
- Git to clone the repository.

### Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
```

**2. Install the dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
python app.py
```

## 🚀 Usage

1. Launch the application in your terminal.
2. Enter the name of a city, such as `Islamabad`, `London`, or `Tokyo`.
3. View the current weather information retrieved for your selected location.

## 🌐 APIs

This project uses the following APIs from Open-Meteo.

- **[Geocoding API](https://open-meteo.com/en/docs/geocoding-api)** — Finds a city's geographic coordinates from its name.
- **[Weather API](https://open-meteo.com/en/docs)** — Retrieves weather data for the selected location.

Both APIs can be used without an API key.

## 📄 License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.
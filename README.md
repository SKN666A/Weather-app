# 🌤️ Weather App

A simple and modern **Weather App** built with Python and Tkinter.
## 📸 Preview

![Weather App Screenshot](weather_app.png)

The app allows users to search for a city and view its current weather information along with a short upcoming-hours forecast.

## ✨ Features

* 🌍 Search weather by city
* 🌡️ Display current temperature
* ☁️ Show current weather condition
* 💧 Display humidity
* 💨 Display wind speed
* 📅 Show short upcoming-hours forecast
* 🖥️ Modern desktop GUI
* ⚠️ Handles invalid cities and API errors

## 🛠️ Technologies Used

* 🐍 Python
* 🖼️ Tkinter
* 🌐 OpenWeather API
* 📦 Requests
* 📁 PyInstaller

## 📁 Project Structure

```text
Weather-app/
│
├── weather_app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 📦 Installation

1. Make sure **Python** is installed.

2. Install the required library:

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

This application uses the **OpenWeather API**.

You need an OpenWeather API key before running the application.

For PowerShell, set your API key as an environment variable:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

**Never publish your real API key in this README or on GitHub.**

## ▶️ How to Run

After setting your API key, run:

```bash
python weather_app.py
```

The Weather App window will open. Enter a city name and click **Search**.

## 🖥️ Windows EXE

A Windows executable can also be created using **PyInstaller**:

```bash
pyinstaller --clean --onefile --windowed weather_app.py
```

The generated `.exe` file will be placed inside the `dist` folder.

> **Note:** The executable still requires access to a valid `OPENWEATHER_API_KEY` environment variable.

## ⚠️ Important

* An internet connection is required.
* A valid OpenWeather API key is required.
* Do not share or commit your API key to GitHub.

## 👩‍💻 Author

**Sakina**

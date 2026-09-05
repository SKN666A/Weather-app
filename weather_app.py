import tkinter as tk
from tkinter import messagebox
import requests
import os

def get_weather():
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        messagebox.showerror(
        "API Key Missing",
        "OPENWEATHER_API_KEY is not set.\nPlease configure your API key before using the app."
    )
        return
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Warning", "Aap ne shehar ka naam enter nahi kiya!")
        return

    # Current Weather API Call
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # Forecast API Call (3 Days / 24 Hours data)
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    try:
        # Current Weather Fetch
        res = requests.get(weather_url)
        data = res.json()

        if data.get("cod") == 200:
            # Current Weather Details
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = round(data["main"]["temp"])
            feels_like = round(data["main"]["feels_like"])
            condition = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = round(data["wind"]["speed"] * 3.6, 1) # m/s to km/h conversion

            # Update Current Weather UI Labels
            location_label.config(text=f"📍 {city_name}, {country}")
            temp_label.config(text=f"{temp}°C")
            condition_label.config(text=f"☁️ {condition} (Feels like {feels_like}°C)")
            humidity_label.config(text=f"💧 Humidity: {humidity}%")
            wind_label.config(text=f"💨 Wind Speed: {wind_speed} km/h")

            # Forecast Fetch
            f_res = requests.get(forecast_url)
            f_data = f_res.json()

            if f_data.get("cod") == "200":
                # Aglay 3 time intervals ka forecast nikalna (Har 3 ghante baad ka data)
                forecast_list = f_data["list"][:3]
                
                f_text1 = f"⏰ {forecast_list[0]['dt_txt'].split()[1][:5]} -> 🌡️ {round(forecast_list[0]['main']['temp'])}°C, {forecast_list[0]['weather'][0]['main']}"
                f_text2 = f"⏰ {forecast_list[1]['dt_txt'].split()[1][:5]} -> 🌡️ {round(forecast_list[1]['main']['temp'])}°C, {forecast_list[1]['weather'][0]['main']}"
                f_text3 = f"⏰ {forecast_list[2]['dt_txt'].split()[1][:5]} -> 🌡️ {round(forecast_list[2]['main']['temp'])}°C, {forecast_list[2]['weather'][0]['main']}"

                fc1_label.config(text=f_text1)
                fc2_label.config(text=f_text2)
                fc3_label.config(text=f_text3)

        elif data.get("cod") == "404":
            messagebox.showerror("Error 404", "❌ Shehar nahi mila! Spelling check karein.")
        elif data.get("cod") == 401:
            messagebox.showerror("Error 401", "❌ Invalid API Key! Sahi key daalein ya activate hone ka wait karein.")
        else:
            messagebox.showerror("Error", f"⚠️ Koi masala aaya: {data.get('message', 'Unknown error')}")

    except Exception:
        messagebox.showerror("Network Error", "❌ Internet connection check karein!")

# --- GUI Window Setup ---
root = tk.Tk()
root.title("Weather App - Modern GUI")
root.geometry("750x850")
root.configure(bg="#282c34") # Dark modern background
root.resizable(False, False)

# Main Title
title_label = tk.Label(root, text="🌤️ Weather App", font=("Helvetica", 18, "bold"), fg="#61afef", bg="#282c34")
title_label.pack(pady=15)

# Search Box Frame
search_frame = tk.Frame(root, bg="#282c34")
search_frame.pack(pady=5)

city_entry = tk.Entry(search_frame, font=("Helvetica", 13), width=20, justify="center")
city_entry.grid(row=0, column=0, padx=5)
city_entry.insert(0, "Multan") # Default city

search_btn = tk.Button(search_frame, text="🔍 Search", font=("Helvetica", 10, "bold"), bg="#98c379", fg="black", command=get_weather, cursor="hand2")
search_btn.grid(row=0, column=1, padx=5)

# Current Weather Card Frame
info_frame = tk.Frame(root, bg="#3e4451", bd=2, relief="groove")
info_frame.pack(fill="x", padx=20, pady=15, ipady=10)

location_label = tk.Label(info_frame, text="📍 City, Country", font=("Helvetica", 24, "bold"), fg="#ffffff", bg="#3e4451")
location_label.pack(pady=3)

temp_label = tk.Label(info_frame, text="--°C", font=("Helvetica", 32, "bold"), fg="#e5c07b", bg="#3e4451")
temp_label.pack()

condition_label = tk.Label(info_frame, text="☁️ Weather Condition", font=("Helvetica", 11), fg="#abb2bf", bg="#3e4451")
condition_label.pack(pady=2)

humidity_label = tk.Label(info_frame, text="💧 Humidity: --%", font=("Helvetica", 10), fg="#ffffff", bg="#3e4451")
humidity_label.pack(pady=2)

wind_label = tk.Label(info_frame, text="💨 Wind Speed: -- km/h", font=("Helvetica", 10), fg="#ffffff", bg="#3e4451")
wind_label.pack(pady=2)

# Forecast Section Frame
forecast_frame = tk.LabelFrame(root, text=" 📅 Short Forecast (Upcoming Hours) ", font=("Helvetica", 10, "bold"), fg="#61afef", bg="#282c34", labelanchor="n")
forecast_frame.pack(fill="x", padx=20, pady=10, ipady=5)

fc1_label = tk.Label(forecast_frame, text="⏰ --:-- -> 🌡️ --°C", font=("Helvetica", 9), fg="#abb2bf", bg="#282c34")
fc1_label.pack(pady=2)

fc2_label = tk.Label(forecast_frame, text="⏰ --:-- -> 🌡️ --°C", font=("Helvetica", 9), fg="#abb2bf", bg="#282c34")
fc2_label.pack(pady=2)

fc3_label = tk.Label(forecast_frame, text="⏰ --:-- -> 🌡️ --°C", font=("Helvetica", 9), fg="#abb2bf", bg="#282c34")
fc3_label.pack(pady=2)

# Start Tkinter Loop
root.mainloop()
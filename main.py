# Jesus Carlos Martinez Gonzalez
# 03/07/2023
# Simple Weather Checker App

# This app was made following this (https://www.youtube.com/watch?v=VaqYFs7Az50&ab_channel=AlinaChudnova) tutorial made by youtuber Alina Chudnova

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


def get_weather(city):
    API_KEY = "your key here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error,", "City not found")
        return None

    # Parsing json response
    weather = res.json()
    icon_id = weather["weather"][0]["icon"]
    temperature = weather["main"]["temp"] - 273.15
    description = weather["weather"][0]["description"]
    city = weather["name"]
    country = weather["sys"]["country"]

    # Get weather icon
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # Update weather icon
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

# Location-entry widget
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Search-button widget
search_button = ttkbootstrap.Button(
    root, text="Search", command=search, bootstyle="warning"
)
search_button.pack(pady=10)

# Location-label widget
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Weather icon label widget
icon_label = tk.Label(root)
icon_label.pack()

# Temperature label widget
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Weather description label widget
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()

import requests
from tkinter import *
import json

curr_weather = None

with open("api_key.txt") as f:
    api_key = f.read()


def get_weather(location, unit):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={unit}')
    data = response.json()

    label = Label(
        root, text=f"City: {location}\n\nConditions: {data['weather'][0]['description']}\n\nTemperature: {data['main']['temp']}{ '°C' if unit == 'metric' else '°F'}\n\nWind: {data['wind']['speed']}{ 'Km/h' if unit == 'metric' else 'Mi/h'} ")
    label.grid(row=5, column=0)


root = Tk()
root.title("Simple Weather App")
root.geometry('600x800')

location_text = Label(root, text="Location").grid(row=0, column=0)
location_entry = Entry(root)
location_entry.grid(row=0, column=1)
unit_text = Label(root, text="Unit").grid(row=1, column=0)
unit_entry = Entry(root)
unit_entry.grid(row=1, column=1)
unit_help = Label(root, text="(metric / imperial)").grid(row=1, column=2)
button = Button(root, text="Get weather",
                command=lambda: get_weather(location_entry.get(), unit_entry.get()))
button.grid(row=3, column=0)

root.mainloop()

import configparser

import requests


class Weather:

    def __init__(self):
        self.config = self.read_config("./resource/application.properties")

    def read_config(self, file_name):
        config = configparser.ConfigParser()
        config.read(file_name)
        return config

    def weather_details_params(self, location):
        return {
            "q": location,
            "appid": self.config['API']['api_key'],
            "units": "metric"  # Change to "imperial" for Fahrenheit
        }

    def get_weather_data(self, location):

        # Make the API request

        params = self.weather_details_params(
            location)

        response = requests.get(self.config['API']['base_url'], params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error:", response.status_code)
            return None

    def display_weather(self, data):
        if data is not None:
            # Extract relevant weather information
            city = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]

            # Display weather information
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed * 3.6} km/h")
            print(f"Description: {description}")
        else:
            print("No data available")

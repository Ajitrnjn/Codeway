from WeatherForecast.weather_details import Weather


def main():
    # Prompt the user for input
    location = input("Enter the name of a city or a zip code: ")

    weather_details = Weather()

    # Get weather data
    weather_data = weather_details.get_weather_data(location)

    # Display weather information
    weather_details.display_weather(weather_data)


if __name__ == "__main__":
    main()

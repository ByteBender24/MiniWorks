import requests

API_KEY = ""

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


def get_weather_emoji(weather_code):
    weather_emojis = {
        "01d": "☀️",  # clear sky (day)
        "01n": "🌙",  # clear sky (night)
        "02d": "⛅️",  # few clouds (day)
        "02n": "🌥",  # few clouds (night)
        "03d": "🌥",  # scattered clouds (day)
        "03n": "🌥",  # scattered clouds (night)
        "04d": "☁️",  # broken clouds (day)
        "04n": "☁️",  # broken clouds (night)
        "09d": "🌧",  # shower rain (day)
        "09n": "🌧",  # shower rain (night)
        "10d": "🌧",  # rain (day)
        "10n": "🌧",  # rain (night)
        "11d": "⛈",  # thunderstorm (day)
        "11n": "⛈",  # thunderstorm (night)
        "13d": "❄️",  # snow (day)
        "13n": "❄️",  # snow (night)
        "50d": "🌫",  # mist (day)
        "50n": "🌫",  # mist (night)
    }
    # Default to question mark if code not found
    return weather_emojis.get(weather_code, "❓")


def display_weather(data):
    city = data["name"]
    weather = data["weather"][0]
    description = weather["description"]
    weather_code = weather["icon"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    emoji = get_weather_emoji(weather_code)

    print(f"Weather in {city}: {description} {emoji}")
    print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def main():
    city = input("Enter city name: ")
    api_key = API_KEY
    print("Fetching weather data...")
    weather_data = get_weather(city, api_key)
    if weather_data["cod"] == 200:
        display_weather(weather_data)
    else:
        print("Error fetching weather data. Please check your city name and API key.")


if __name__ == "__main__":
    main()

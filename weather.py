import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather in {city}: {weather_desc}, Temperature: {temperature}°C")
    else:
        print("Failed to fetch weather data. Please check your city name.")

def main():
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
    city = input("Enter city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()

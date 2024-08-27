from dotenv import load_dotenv
from pprint import pprint
import requests
import os 

load_dotenv()

def get_current_weather(city='nagercoil'):
    
    requests_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_URL")}&units=imperial'
    weather_data = requests.get(requests_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n *** Get Current Weather Conditions ***")

    city = input("\n Please enter a city name:")
    #check for empty strings or strings with spaces
    if not bool(city.strip()):
        city = 'nagercoil'
    weather_data = get_current_weather(city)

    print('\n')

    pprint(weather_data)
    
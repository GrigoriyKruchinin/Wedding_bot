import os
import httpx
from dotenv import load_dotenv
from translate import Translator
from pydantic import BaseModel

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


class Weather(BaseModel):
    lat: float
    lon: float
    temp_celsius: float
    description_ru: str


async def get_weather(lat, lon):
    base_url = WEATHER_URL
    params = {
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        weather_data = response.json()

        weather_model = Weather(
            lat=weather_data['coord']['lat'],
            lon=weather_data['coord']['lon'],
            temp_celsius=round(weather_data['main']['temp'] - 273.15, 1),
            description_ru=Translator("ru").translate(
                weather_data['weather'][0]['description']
            )
        )
        return weather_model

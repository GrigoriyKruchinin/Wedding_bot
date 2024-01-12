import os

from dotenv import load_dotenv
import httpx
from translate import Translator

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


async def get_weather(lat, lon):
    base_url = WEATHER_URL
    params = {
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Не удалось получить данные о погоде 🫣")

        weather_data = response.json()
        t_kelvin = weather_data['main']['temp']
        t_celsius = round(t_kelvin - 273.15, 1)
        description_eng = weather_data['weather'][0]['description']
        translator = Translator("ru")
        description_ru = translator.translate(description_eng)
        return t_celsius, description_ru

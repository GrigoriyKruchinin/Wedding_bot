import os
import asyncio
import logging
from datetime import datetime

import httpx
from dotenv import load_dotenv

from translate import Translator
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command


load_dotenv()

TOKEN = os.getenv('TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API')

bot = Bot(TOKEN)
dp = Dispatcher()

WEDDING_DATE = datetime(2024, 8, 24)

# Координаты Оленьих Прудов
LAT, LON = 56.466166, 41.552384

GREETING_MESSAGE = (
    "Привет, {username}!\n"
    "Я бот для получения информации о свадьбе Гриши и Лены!\n"
    "Для получения общей информации воспользуйтесь командой /info\n"
    "Попробуйте все команды, не стесняйтесь!\n"
)

INFO_MESSAGE = (
    "Стиль такой-то\n"
    "Без детей\n"
    "Не дарите скороварки, мы живем за границей - не увезем!\n"
    "Сбор там-то\n"
    "Телефоны организаторов: ____"
    "И другая инфа!"
)

DAYS_LEFT_MESSAGE = (
    "До знаменательной даты осталось {days_count} {days_word}!!!\n"
    "Еще чуть-чуть и вы сможете поплакать над тем, "
    "какие Гриша и Лена милые 🥰🥰🥰\n"
    "Ну и отдохнуть и повеселиться от души 🍾🍾🍾\n"
)

FALLBACK_MESSAGE = (
    'Для получения информации о свадьбе Гриши и Лены '
    'воспользуйтесь встроенными командами!\n'
)

STICKER_DOG = (
    "CAACAgIAAxkBAAELIitlnrqebILw4fRZ1TxmDvhm6SFo6AACfwEAAj0N6AS98XKpqDIlKDQE"
)


async def get_weather(lat, lon):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        weather_data = response.json()
        t_kelvin = weather_data['main']['temp']
        t_celsius = round(t_kelvin - 273.15, 1)
        description_eng = weather_data['weather'][0]['description']
        translator = Translator("ru")
        description_ru = translator.translate(description_eng)
        return t_celsius, description_ru


@dp.message(Command('weather'))
async def weather(message: Message):
    temperature, description = await get_weather(LAT, LON)
    await message.answer(
        f"Погода сейчас:\nТемпература: {temperature}\nОписание: {description}"
    )


@dp.message(CommandStart())
async def start(message: Message):
    username = message.from_user.full_name
    await message.answer(text=GREETING_MESSAGE.format(username=username))
    await bot.send_sticker(chat_id=message.chat.id, sticker=STICKER_DOG)


@dp.message(Command('info'))
async def info(message: Message):
    await message.answer(text=INFO_MESSAGE)


@dp.message(Command('days_left'))
async def days_until_wedding(message: Message):
    days_count = (WEDDING_DATE - datetime.now()).days
    days_word = ("дней" if days_count % 10 in {0, 5, 6, 7, 8, 9}
                or (11 <= days_count <= 19) else "дня")  # noqa
    await message.answer(
        DAYS_LEFT_MESSAGE.format(days_count=days_count, days_word=days_word)
    )


@dp.message()
async def answer(message: Message):
    await message.answer(text=FALLBACK_MESSAGE)
    await bot.send_sticker(chat_id=message.chat.id, sticker=STICKER_DOG)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

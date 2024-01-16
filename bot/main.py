import os
import asyncio
import logging
from datetime import datetime

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart, Command

from messages import (
    GREETING_MESSAGE, INFO_MESSAGE, DAYS_LEFT_MESSAGE, TODAY_WEDDING,
    WEDDING_WAS_OVER, WEATHER_MESSAGE, FALLBACK_MESSAGE, STICKER_DOG
)
from weather_utils import get_weather

load_dotenv()

TOKEN = os.getenv('TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API')

bot = Bot(TOKEN)
dp = Dispatcher()
router = Router()

WEDDING_DATE = datetime(2024, 8, 24)  # Дата свадьбы
LAT, LON = 56.466166, 41.552384  # Координаты Оленьих Прудов


@router.message(CommandStart())
async def start(message: types.Message):
    username = message.from_user.full_name
    await message.answer(text=GREETING_MESSAGE.format(username=username))
    await bot.send_sticker(chat_id=message.chat.id, sticker=STICKER_DOG)


@router.message(Command('info'))
async def info(message: types.Message):
    await message.answer(text=INFO_MESSAGE)


@router.message(Command('weather'))
async def weather(message: types.Message):
    weather_info = await get_weather(LAT, LON)
    await message.answer(
        WEATHER_MESSAGE.format(
            temperature=weather_info.temp_celsius,
            description=weather_info.description_ru
        )
    )


@router.message(Command('days_left'))
async def days_until_wedding(message: types.Message):
    days_count = (WEDDING_DATE - datetime.now()).days
    days_word = ("дней" if days_count % 10 in {0, 5, 6, 7, 8, 9}
                or (11 <= days_count <= 19) else "дня")  # noqa
    if days_count > 0:
        await message.answer(
            DAYS_LEFT_MESSAGE.format(
                days_count=days_count,
                days_word=days_word
            )
        )
    elif days_count == 0:
        await message.answer(TODAY_WEDDING)
    else:
        await message.answer(WEDDING_WAS_OVER)


@router.message()
async def answer(message: types.Message):
    await message.answer(text=FALLBACK_MESSAGE)
    await bot.send_sticker(chat_id=message.chat.id, sticker=STICKER_DOG)


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

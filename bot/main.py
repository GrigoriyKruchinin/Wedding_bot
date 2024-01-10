import os
import asyncio
import logging

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command

from bot.helpers.stickers_id import STICKER_DOG


load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message):
    username = message.from_user.full_name
    await message.answer(text=f'Привет, {username}!')
    await message.answer(
        text='Это тг бот для получения информации о свадьбе Гриши и Лены!'
    )
    await message.answer(
        text=(
            'Для получение общей информации воспользуйтесь командой /help'
        )
    )
    await message.answer(
        text=(
            "Но я умею не только это 🫣 "
            "Попробуйте все команды, не стесняйтесь!" 
        )
    )
    await bot.send_sticker(chat_id=message.chat.id, sticker=STICKER_DOG)


@dp.message(Command('help'))
async def help(message):
    await message.answer("Тут будет выводиться инфо о свадьбе")


@dp.message()
async def answer(message):
    await message.reply(
        text=(
            'Для получения информации о свадьбе Гриши и Лены '
            'воспользуйтесь встроенными командами!'
        )
    )
    await bot.send_sticker(chat_id=message.chat.id, sticker=STICKER_DOG)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

import os
import asyncio

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command




load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message()
async def main():
    pass


if __name__ == "__main__":
    asyncio.run(main())

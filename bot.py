import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7792198103:AAEiYwnXqVeKLs8zi5Sr9ZrwWP-Vq_XbJCs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я твой Telegram-бот ⚡")

@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("Я умею писать команду /start")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
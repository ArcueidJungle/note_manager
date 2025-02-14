import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загрузка переменных окружения (если используете .env)
load_dotenv()

bot = Bot(token=TOKEN)
dp = Dispatcher()  # Создаем диспетчер

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я работающий бот!")

# Обработчик всех текстовых сообщений
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
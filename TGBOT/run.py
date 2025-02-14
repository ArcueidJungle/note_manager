import asyncio

import requests

from config import TOKEN, OWM_API_KEY
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Загрузка переменных окружения (если используете .env)
load_dotenv()

bot = Bot(token=TOKEN)
dp = Dispatcher()  # Создаем диспетчер

weather_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Москва"), KeyboardButton(text="Санкт-Петербург")],
        [KeyboardButton(text="Новосибирск"), KeyboardButton(text="Другой город")]
    ],
    resize_keyboard=True  # Кнопки подстраиваются под размер экрана
)



def get_weather(city: str) -> str:
    # Формируем URL-запрос
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=ru"

    # Отправляем запрос
    response = requests.get(url)
    data = response.json()

    # Проверяем статус ответа
    if response.status_code != 200:
        return f"⚠️ Ошибка: {data['message']}"

    # Извлекаем данные
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    # Форматируем ответ
    return (
        f"🌤 Погода в {city}:\n"
        f"• Температура: {temp}°C\n"
        f"• Состояние: {description}\n"
        f"• Влажность: {humidity}%"
    )


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🌤 Выберите город или введите название:",
                         reply_markup = weather_kb
                        )

CITIES = ["Москва", "Санкт-Петербург", "Новосибирск"]

@dp.message(lambda message: message.text in CITIES)
async def handle_city_button(message: types.Message):
    city = message.text
    try:
        weather_info = get_weather(city)
    except Exception as e:
        weather_info = f"⚠️ Ошибка: {e}"
    await message.answer(weather_info, reply_markup=weather_kb)


@dp.message(lambda message: message.text == "Другой город")
async def handle_other_city(message: types.Message):
    await message.answer("Введите название города:")

@dp.message(lambda message: message.text not in CITIES + ["Другой город"])
async def handle_custom_city(message: types.Message):
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❌ Укажите город, например: /weather Москва")
        return

    city = " ".join(parts[1:])
    try:
        weather_info = get_weather(city)
    except Exception as e:
        weather_info = f"⚠️ Ошибка: {e}"
    await message.answer(weather_info)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
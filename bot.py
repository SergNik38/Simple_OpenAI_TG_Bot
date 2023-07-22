import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from conversation import Conversation

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global chat
    chat = Conversation()
    await message.reply('Привет я отвечу на все твои вопросы')


@dp.message_handler()
async def answer(message: types.Message):
    chat.add_message('user', message.text)
    await message.answer('1')


if __name__ == '__main__':
    executor.start_polling(dp)

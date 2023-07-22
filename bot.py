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
    chat = Conversation(model='gpt-3.5-turbo')
    await message.reply('Привет я отвечу на все твои вопросы')


@dp.message_handler()
async def answer(message: types.Message):
    chat.add_message('user', message.text)
    response = chat.create_conversation()
    chat.add_message('assistant', response['choices'][0]['message']['content'])
    await message.answer(chat.messages[-1]['content'])


if __name__ == '__main__':
    executor.start_polling(dp)

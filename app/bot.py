import os

import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatActions, ContentType
from dotenv import load_dotenv
from app import keyboards as kb

from app.conversation import Conversation

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        'Привет! Я бот с технологией ChatGPT \nТы можешь общаться со мной как голосом так и текстом! \nВыбери доступную команду.',
        reply_markup=kb.main)


@dp.message_handler(text='Генерировать текст')
async def generate(message: types.Message):
    global chat
    chat = Conversation(model='gpt-3.5-turbo')
    await message.reply('Беседа создана', reply_markup=kb.text_kb)


@dp.message_handler(text='Генерировать изображение')
async def generate(message: types.Message):
    await message.reply('Пока недоступно')


@dp.message_handler(text='Новая беседа')
async def new_conversation(message: types.Message):
    chat.new_conversation()
    await message.answer('Контекст удален', reply_markup=kb.text_kb)


@dp.message_handler()
async def answer(message: types.Message):
    await bot.send_chat_action(message.from_user.id, ChatActions.TYPING)
    try:
        chat.add_message('user', message.text)
        response = chat.create_conversation()
        chat.add_message('assistant', response['choices'][0]['message']['content'])
        await message.answer(chat.messages[-1]['content'])
    except Exception:
        await message.answer('Выберите доступную команду', reply_markup=kb.main)


@dp.message_handler(content_types=ContentType.VOICE)
async def voice_message_handler(message: types.Message):
    await bot.send_chat_action(message.from_user.id, ChatActions.TYPING)
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    f_name = f'{file_id}.oga'
    await bot.download_file(file.file_path, f_name)
    with open(f_name, 'rb') as audio_file:
        message.text = openai.Audio.transcribe('whisper-1', audio_file)['text']
    os.remove(f_name)
    await answer(message)

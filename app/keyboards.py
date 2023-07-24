from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Генерировать текст', "Генерировать изображение")

text_kb = ReplyKeyboardMarkup(resize_keyboard=True)
text_kb.add('Новая беседа')


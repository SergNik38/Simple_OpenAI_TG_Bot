import os
from dotenv import load_dotenv
from app import bot
import threading

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

if __name__ == '__main__':
    thread = threading.Thread(target=bot.executor.start_polling(bot.dp, skip_updates=True))
    thread.start()

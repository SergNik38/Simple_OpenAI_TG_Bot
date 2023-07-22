import os
import openai
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

openai.api_key = os.getenv('OPENAI_API_KEY')


class Conversation:
    def __init__(self, model):
        self.model = model
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({
            'role': role, 'content': content
        })

    def create_conversation(self):
        return openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )



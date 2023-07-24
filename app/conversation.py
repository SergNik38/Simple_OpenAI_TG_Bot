import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


class Conversation:
    """
    ChatGPT conversation
    """

    def __init__(self, model):
        self.model = model
        self.messages = []

    def add_message(self, role, content):
        """
        Adds new message to the conversation
        :param role:
        :param content:
        :return:
        """
        self.messages.append({
            'role': role, 'content': content
        })

    def create_conversation(self):
        """
        Starts a new conversation
        :return:
        """
        return openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )

    def new_conversation(self):
        """
        Removes the context
        :return:
        """
        self.messages = []

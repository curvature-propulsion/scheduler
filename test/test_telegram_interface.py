import unittest
from unittest.mock import MagicMock
from telegram_interface import TelegramBot

class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.token = 'fake-token'
        self.bot = TelegramBot(self.token)
        self.bot.updater = MagicMock()
        self.bot.dispatcher = MagicMock()

    def test_start(self):
        update = MagicMock()
        context = MagicMock()
        self.bot.start(update, context)
        context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id, text="Hello! I am a bot.")

    def test_echo(self):
        update = MagicMock()
        update.message.text = "Hello"
        context = MagicMock()
        self.bot.echo(update, context)
        context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id, text="Hello")

if __name__ == '__main__':
    unittest.main()

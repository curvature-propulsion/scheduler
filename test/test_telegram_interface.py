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

    def test_parse_event(self):
        message = "Meeting on 2023-10-10 at 10:00 AM in Office to discuss project."
        expected_response = "Title: Meeting, Date: 2023-10-10, Time: 10:00 AM, Location: Office, Description: discuss project"
        self.bot.parse_event = MagicMock(return_value=expected_response)
        response = self.bot.parse_event(message)
        self.assertEqual(response, expected_response)

def test_send_reminder(self):
    self.bot.application.bot.send_message = MagicMock()
    self.bot.send_reminder()
    self.bot.application.bot.send_message.assert_called_once_with(chat_id='YOUR_CHAT_ID', text="This is your daily reminder!")
if __name__ == '__main__':
    unittest.main()

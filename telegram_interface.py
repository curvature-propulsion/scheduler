import telegram
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai


class TelegramBot:
    def __init__(self, token):
        self.application = ApplicationBuilder().token(token).build()

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am a bot.")

    def handle_message(self, update, context):
        message = update.message.text
        event_details = self.parse_event(message)
        context.bot.send_message(chat_id=update.effective_chat.id, text=event_details)

    def run(self):
        start_handler = CommandHandler('start', self.start)
        message_handler = MessageHandler(Filters.text & (~Filters.command), self.handle_message)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(message_handler)
def parse_event(self, message):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Extract event details from the following message: {message}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    bot = TelegramBot(TOKEN)
    bot.run()

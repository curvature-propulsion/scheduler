import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TelegramBot:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am a bot.")

    def echo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def run(self):
        start_handler = CommandHandler('start', self.start)
        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(echo_handler)
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    bot = TelegramBot(TOKEN)
    bot.run()

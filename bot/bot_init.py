import telepot
from telepot.loop import MessageLoop


class BotInit:

    def __init__(self, telegram_token):
        self.bot = telepot.Bot(telegram_token)
        self.run_bot()

    def run_bot(self):
        print('Your bot is running...')
        MessageLoop(self.bot, self.print_message).run_forever()

    def print_message(self, message):
        print(f"Receiving message from {message['from']['first_name']} with text: '{message['text']}'")
        self.bot.sendMessage(message['from']['id'], f"You inputted '{message['text']}'")

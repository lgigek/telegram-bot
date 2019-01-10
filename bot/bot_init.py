import telepot
from telepot.loop import MessageLoop


class BotInit:

    def __init__(self, telegram_token):
        self.bot = telepot.Bot(telegram_token)
        self.run_bot()

    def run_bot(self):
        print('Your bot is running...')
        MessageLoop(self.bot, self.handler).run_forever()

    def handler(self, message):
        print(f"Receiving message from {message['from']['first_name']}({message['from']['id']}) with text: "
              f"'{message['text']}'")
        self.print_message(message['from']['id'], message['text'])

    def print_message(self, user_id, message):
        print(f"Sending '{message}' to '{user_id}'")
        self.bot.sendMessage(user_id, f"You inputted '{message}'")

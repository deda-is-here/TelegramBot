import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


def user_greeting(update, context):
    print('/start был вызван')
    update.message.reply_text("Привет, ты нажал кнопку")


def echo_talking (update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", user_greeting))
    dp.add_handler(MessageHandler(Filters.text, echo_talking))

    logging.info('бот стартовал')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

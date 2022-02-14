from datetime import datetime
import ephem
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


def user_greeting(update, context):
    print('/start был вызван')
    update.message.reply_text("Привет, ты нажал кнопку")


def planet_info(update, context):
    input_planet = update.message.text.split(' ')[1]
    if input_planet == "Mercury":
        planet = ephem.Mercury(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Venus":
        planet = ephem.Venus(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Earth":
        planet = ephem.Earth(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Mars ":
        planet = ephem.Mars(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Jupiter":
        planet = ephem.Jupiter(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Saturn":
        planet = ephem.Saturn(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Uranus":
        planet = ephem.Uranus(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif input_planet == "Neptune":
        planet = ephem.Neptune(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    else:
        update.message.reply_text("Такой планеты нет")


def echo_talking(update, context):
    text = update.message.text
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", user_greeting))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, echo_talking))

    logging.info('бот стартовал')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

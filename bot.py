from datetime import datetime, date
from emoji import emojize
import ephem
from glob import glob
import logging
from random import randint, choice
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from cities import city_list


logging.basicConfig(filename='bot.log', level=logging.INFO)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data["emoji"]


def user_greeting(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Привет! {context.user_data['emoji']}")


def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!'
    elif user_number < bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, я выиграл!'
    else:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ничья!'
    return message


def digit_guess(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)


def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.sendPhoto(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))


# def cities_game(update, context):
#
#     def city_finder(letter, arr):
#         for word in arr:
#             for _ in word:
#                 if word[0].lower() == letter.lower():
#                     return word
#
    # def playtime():
    #     city = update.message.text.split(' ')[1]
    #     flag = True
    #     while flag:
    #         cities_filtered = city_list()
    #         try:
    #             if city not in cities_filtered and city != 'Я сдаюсь':
    #                 update.message.reply_text('Этого города не существует, введите другой')
    #                 city = update.message.text
    #             elif city == "Я сдаюсь":
    #                 update.message.reply_text('Вы проиграли!')
    #                 update.message.reply_text('Хотите сыграть еще? Да/Нет?')
    #                 flag_quest = update.message.text
    #                 if flag_quest.lower() == 'да':
    #                     playtime()
    #                 elif flag_quest.lower() == 'нет':
    #                     flag = False
    #             else:
    #                 cities_filtered.remove(city)
    #                 city_bot = city_finder(city[-1], cities_filtered)
    #                 cities_filtered.remove(city_bot)
    #                 update.message.reply_text(f'{city_bot}, ваш ход')
    #                 city = update.message.text
    #                 while city[0].lower() != city_bot[-1].lower() and city != "Я сдаюсь":
    #                     update.message.reply_text(f'Введите слово на букву {city_bot[-1].upper()} - ')
    #                     city = update.message.text
    #         except ValueError:
    #             update.message.reply_text('Вы победили!\nХотите сыграть еще? Да/Нет?')
    #             flag_quest = update.message.text
    #             if flag_quest.lower() == 'да':
    #                 playtime()
    #             elif flag_quest.lower() == 'нет':
    #                 flag = False
    # playtime()


# def calculator(update, context):
#     text = update.message.text.split(' ')[1]
#     if len(text) != 3:
#         update.message.reply_text('Строка должна быть длинной 3 символа')
#         raise ValueError('Больше знаков, чем допустимо программой')
#     else:
#         if text[0].isdigit() and text[2].isdigit():
#             if text[1] == "+":
#                 update.message.reply_text(float(text[0]) + float(text[2]))
#             if text[1] == "-":
#                 update.message.reply_text(float(text[0]) - float(text[2]))
#             if text[1] == "*":
#                 update.message.reply_text(float(text[0]) * float(text[2]))
#             if text[1] == "/":
#                 if text[2] == '0':
#                     update.message.reply_text('На ноль делить нельзя')
#                     raise ZeroDivisionError('поделили на ноль')
#                 else:
#                     update.message.reply_text(float(text[0]) / float(text[2]))
#         else:
#             update.message.reply_text('введите числовое значение')
#             raise TypeError('ввели не число')


def word_counter(update, context):
    text = update.message.text
    if text.isdigit():
        update.message.reply_text('Введите слова!')
    elif not context.args:
        update.message.reply_text('Пустую строку нельзя')
        raise ValueError('Передали пустую строку')
    elif len(text) > 250:
        update.message.reply_text('Слишком большая строка')
        raise ValueError('Передали слишком большую строку')
    else:
        update.message.reply_text(f'{len(text.strip().split(" ")) - 1} слова')


def next_full_moon(update, context):
    moon_date = datetime.now()
    update.message.reply_text(f'Следующая полная луна {ephem.next_full_moon(moon_date)}')


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
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")


def main():
    mybot = Updater(settings.API_KEY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", user_greeting, run_async=True))
    dp.add_handler(CommandHandler("planet", planet_info, run_async=True))
    dp.add_handler(CommandHandler("wordcount", word_counter, run_async=True))
    dp.add_handler(CommandHandler("full_moon", next_full_moon, run_async=True))
    dp.add_handler(CommandHandler("guess", digit_guess, run_async=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    # dp.add_handler(CommandHandler("cities", cities_game, run_async=True))
    # dp.add_handler(CommandHandler("calc", calculator, run_async=True))
    dp.add_handler(MessageHandler(Filters.text, echo_talking, run_async=True))

    logging.info('бот стартовал')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

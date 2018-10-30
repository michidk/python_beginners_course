import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from weather import Weather, Unit


def hi(bot, update):
    update.message.reply_text('Hi!')


def weather_info(bot, update, args):
    if not args:
        location_name = 'Munich'
    else:
        location_name = args[0]
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(location_name)
    wetter = "Morgen Wetter in " + location_name + ": " + location.forecast[1].text
    temperatur = " und Temperatur: " + str(location.forecast[1].low) + ' *C'
    update.message.reply_text(wetter + temperatur)


def main(token):
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("hi", hi))
    dp.add_handler(CommandHandler("wetter", weather_info, pass_args=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main(sys.argv[1])

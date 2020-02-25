"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import datetime
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PLANETS = {'Mercury':ephem.Mercury, 
             'Venus':ephem.Venus, 
              'Mars':ephem.Mars, 
           'Jupiter':ephem.Jupiter, 
            'Saturn':ephem.Saturn, 
            'Uranus':ephem.Uranus, 
           'Neptune':ephem.Neptune, 
             'Pluto':ephem.Pluto, 
               'Sun':ephem.Sun, 
              'Moon':ephem.Moon, }

def greet_user(bot, update):
    text = 'Вызван /start'
    update.message.reply_text(text)


def get_planet(bot, update):
    answer = 'Не знаю такую планету'
    today = datetime.datetime.now().strftime('%Y/%d/%m')
    planet_name = update.message.text.split()
    if len(planet_name) > 1 and planet_name[1].capitalize() in PLANETS:
        planet = PLANETS[planet_name[1].capitalize()](today)
        update.message.reply_text('{} :: {}'.format(today, ephem.constellation(planet)))
    else:
        update.message.reply_text(answer)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.BOT_TOKEN, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher  
    dp = mybot.dispatcher  
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()

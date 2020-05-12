import COVID19Py
import telebot

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1207902294:AAFvSeiYWScIxuBfG6uGy3bSp1XIMid0M2M')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

    bot.polling(none_stop=True)

#location = covid19.getLocationByCountryCode("US")
#latest = covid19.getLatest()


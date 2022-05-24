import os
import telebot
from decouple import config
import yfinance as yf

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hey! This bot is built by Archit :D")\

# @bot.message_handler(commands=['hola'])
# def hola(message):
#     bot.send_message(message.chat.id, 'holaaaaaaaa')

def stock_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True

@bot.message_handler(func=stock_request)
def send_price(message):
    request = message.text.split()[1]
    data = yf.download(tickers=request, period='5m', interval='1m')
    if data.size>0:
        bot.send_message(message.chat.id, 'UTC time is mentioned')
        # data=data.reset_index()
        # data['format_date'] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
        # data.set_index('format_date', inplace=True)
        # print(data.to_string())
        # bot.send_message(message.chat.id, data['close'].to_string(header=False))
        bot.send_message(message.chat.id, data)

    else:
        bot.send_message(message.chat.id, 'No data available :(')


print('running')
bot.polling()  # keeps checking for response
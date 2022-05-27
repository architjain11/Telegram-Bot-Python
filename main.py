import os
import telebot
from decouple import config
import yfinance as yf

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hey! This bot is built by Archit :D\nType 'price' followed by the ticker to get the current price.\nEg. price tsla (returns current stock price of Tesla Inc.)")

def stock_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        bot.send_message(message.chat.id, "Invalid Input. Try using:\nprice <ticker>")
        return False
    else:
        return True

@bot.message_handler(func=stock_request)
def send_price(message):
    request = message.text.split()[1]
    data = yf.download(tickers=request, period='5m', interval='1m')
    if data.size>0:
        price = data['Close'].iloc[-1]
        msg = 'Current stock price for ' + request + ' is: ' + str(round(price,2))
        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, 'No data available :(')

print('running')
bot.polling()
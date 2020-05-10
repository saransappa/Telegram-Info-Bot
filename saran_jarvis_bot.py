import telebot
import time 
import requests, json 
from forex_python.converter import CurrencyRates
c = CurrencyRates()
from datetime import date
bot_token = '<telegram-bot-token>' # Enter your own telegram bot token

bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome to currency exchange bot.')

@bot.message_handler(commands=['help'])
def send_help(message):
    msg = """ Currency Codes:
USD    -->    US dollar	
JPY    -->    Japanese yen	
BGN	   -->    Bulgarian lev	
CZK	   -->    Czech koruna	
DKK	   -->    Danish krone	
GBP	   -->    Pound sterling	
HUF	   -->    Hungarian forint	
PLN	   -->    Polish zloty	
RON	   -->    Romanian leu	
SEK	   -->    Swedish krona	
CHF	   -->    Swiss franc	
ISK	   -->    Icelandic krona
NOK	   -->    Norwegian krone
HRK	   -->    Croatian kuna
RUB	   -->    Russian rouble	
TRY	   -->    Turkish lira	
AUD	   -->    Australian dollar	
BRL	   -->    Brazilian real	
CAD	   -->    Canadian dollar	
CNY	   -->    Chinese yuan renminbi
HKD	   -->    Hong Kong dollar	
IDR	   -->    Indonesian rupiah	
ILS	   -->    Israeli shekel	
INR	   -->    Indian rupee	
KRW	   -->    South Korean won
MXN	   -->    Mexican peso	
MYR	   -->    Malaysian ringgit
NZD	   -->    New Zealand dollar
PHP	   -->    Philippine peso
SGD	   -->    Singapore dollar	
THB	   -->    Thai baht
ZAR	   -->    South African rand"""
    bot.reply_to(message,msg+'\n\n\nTo use this bot, send the request in the following format: \n <from_currency_code> <to_currency_code> <value_in_from_currency>\n\nEnter "/source" (without quotes) to see my source. ')

@bot.message_handler(commands=['source'])
def send_source(message):
    bot.reply_to(message,"https://ratesapi.io/")

@bot.message_handler(func = lambda m: True)
def send_Ans(message):
    text = str(message.text).split()
    if len(text)!=3:
        bot.reply_to(message,'Please use the correct format for currency conversion. Enter "/help" to get help.')
    else:
        try:
            bot.reply_to(message,c.convert(text[0],text[1],float(text[2])))
        except:
            bot.reply_to(message,"Sorry! Can't convert now. Please try again later")

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
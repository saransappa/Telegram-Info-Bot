import telebot
import time
from forex_python.converter import CurrencyRates
c = CurrencyRates()
bot_token = '1218807901:AAHA8XsR-ziVK6jtToLebY43f2TVTSZ-hM0'

bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Hi "+message.chat.first_name)
    bot.reply_to(message,'Welcome to weather and currency exchange bot.\nEnter "/help"(without quotes) to get some help.')

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
    bot.reply_to(message,msg+'\n\n\nTo use this bot, send the request in the following format(without brackets): \n "/currency <from_currency_code> <to_currency_code> <value_in_from_currency>"\n\nEnter "/source" (without quotes) to see my source. \n\n Use "/weather <location_name>" (State can be written in short form if there are more cities with same name. State should be separated with a comma but there should be no spaces.) to get the weather report. \n\n Use "/ping" to check the status of the bot.')

@bot.message_handler(commands=['source'])
def send_source(message):
    bot.reply_to(message,"For currency exchange: https://ratesapi.io/ \n For weather report: https://wttr.in")

@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")

@bot.message_handler(commands=['name'])
def send_name(message):
    bot.reply_to(message,"Your name is "+message.chat.first_name+" "+message.chat.last_name)


@bot.message_handler(commands=['weather'])
def send_weather(message):
    try:
        k = message.text.split()[1]
        bot.reply_to(message,"wttr.in/"+k)
    except:
        bot.reply_to(message,"Please enter a location name to get the weather report.")

@bot.message_handler(commands=['currency'])
def send_Ans(message):
    text = str(message.text).split()
    if len(text)!=4:
        bot.reply_to(message,'Please use the correct format for weather report or currency conversion. \nEnter  "/help" to get help.')
    else:
        try:
            bot.reply_to(message,str(c.convert(text[1],text[2],float(text[3])))+" "+text[2])
        except:
            bot.reply_to(message,"Sorry! Can't convert now. Please try again later")




while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

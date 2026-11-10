import os
import telebot

TOKEN = '9066354751:AAECGYn8LIAzpaYS6XEa0Kego3d7WDqfFps'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! بوت زيادة التفاعل والإنستغرام يعمل بنجاح ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "استلمت رسالتك وجاري معالجة الطلب...")

bot.infinity_polling()
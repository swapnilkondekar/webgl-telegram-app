import os
import telebot
from telebot import types

# Placeholder for bot token - you'll replace this when running locally
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a web app keyboard button
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = types.KeyboardButton(
        "Play Game", 
        web_app=types.WebAppInfo(url="https://swapnilkondekar.github.io/webgl-telegram-app/")
    )
    markup.add(web_app_button)
    
    bot.reply_to(message, 
        "Welcome! Click the button below to play the game.", 
        reply_markup=markup
    )

# Start the bot
if __name__ == '__main__':
    bot.polling()
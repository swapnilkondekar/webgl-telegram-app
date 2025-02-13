import os
import telebot
from telebot import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Telegram Web App URL (update with your actual GitHub Pages URL)
WEB_APP_URL = 'https://swapnilkondekar.github.io/webgl-telegram-app/'

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a keyboard with a web app button
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_info = types.WebAppInfo(url=WEB_APP_URL)
    web_app_button = types.KeyboardButton(
        text='🎮 Play Game', 
        web_app=web_app_info
    )
    markup.add(web_app_button)
    
    welcome_message = (
        "Welcome to the WebGL Telegram Game! 🎲\n\n"
        "Click the 'Play Game' button below to start your adventure!"
    )
    
    bot.reply_to(message, welcome_message, reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    try:
        # Optional: Process any data sent back from the web app
        if message.web_app_data:
            bot.reply_to(message, "Game data received successfully!")
    except Exception as e:
        bot.reply_to(message, f"Error processing game data: {e}")

# Error handling
def main():
    try:
        print("Bot is running...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Bot encountered an error: {e}")

if __name__ == '__main__':
    main()
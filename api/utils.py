import os 
import telebot

def find_models(dir, file_name):
    for _, _, files in os.walk(dir):
        if file_name in files:
            return True
    
    return False

def send_telegram_message(bot_token: str, chat_id: int, message: str):
    bot = telebot.TeleBot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)
import telebot
import os
from handlers import bot_handlers
from flask import Flask, request

TOKEN = '8877859402:AAESVv6dFFHoSwni-WqcW2jTqNRlCDRYyo8'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_str = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot_handlers(bot)
    bot.remove_webhook()
    bot.set_webhook(url="https://italian-bot-final.onrender.com/" + TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

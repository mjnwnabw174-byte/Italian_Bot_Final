import telebot
from handlers import bot_handlers
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# إعداد المعالجات
bot_handlers(bot)

print("الوحش يعمل الآن...")
bot.infinity_polling()

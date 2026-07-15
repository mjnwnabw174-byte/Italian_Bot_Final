import telebot
from config import TOKEN
import handlers  # استيراد ملف الأزرار
import logic     # استيراد ملف المنطق

bot = telebot.TeleBot(TOKEN)

# تفعيل الأزرار والمنطق
handlers.bot_handlers(bot) 

print("الوحش يعمل بكامل طاقته...")
bot.infinity_polling()

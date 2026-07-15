import telebot
from config import TOKEN
import handlers
import logic

# تشغيل البوت
bot = telebot.TeleBot(TOKEN)

# تفعيل الأزرار والمنطق (شغلك الحقيقي)
handlers.bot_handlers(bot)

# الضربة القاضية: مسح التخبيص القديم والتشغيل
if __name__ == "__main__":
    print("الوحش يعمل الآن وبكامل قوته...")
    bot.delete_webhook()
    bot.infinity_polling()

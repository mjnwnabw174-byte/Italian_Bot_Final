import telebot
from config import TOKEN
import handlers
import logic

# تشغيل البوت
bot = telebot.TeleBot(TOKEN)

# نربط الهاندلرز بالبوت ونمرر البوت للمنطق عشان يقدر يرسل ويستقبل بيانات من الشيتس
handlers.bot_handlers(bot)

# عند بدء التشغيل، البوت الآن جاهز للعمل مع "المخ"
if __name__ == "__main__":
    print("شبل حجة يعمل الآن... والجيش يستعد للتفاعل!")
    
    # تسجيل حالة تشغيل البوت في الشيتس (اختياري، لتعرف متى عمل ريستارت)
    try:
        logic.log_to_sheets("System", "System", "البوت اشتغل الآن 🚀")
    except:
        pass
        
    bot.delete_webhook()
    bot.infinity_polling()

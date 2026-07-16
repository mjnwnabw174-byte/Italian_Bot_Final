import telebot
import logic
from config import MY_ID  # تأكد أن MY_ID موجودة في ملف config.py

def bot_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        # تسجيل دخول في الشيتس (سجل الحضور)
        logic.log_to_sheets(user.first_name, user.username or "لا يوجد", "انضم للبوت")
        
        # إشعار واحد لك أنت (الرسالة الواحدة اللي طلبتها)
        bot.send_message(MY_ID, f"🟢 انضمام جديد:\nالاسم: {user.first_name}\nاليوزر: @{user.username or 'لا يوجد'}\nالآي دي: {user.id}")
        
        welcome_text = (
            "🔥 أهلاً بك يا وحش في جيش إيطالي! 🔥\n\n"
            "القاعدة الذهبية: تفاعل مع 3 فيديوهات (لايك + تعليق + إكسبلور)، وبتشوف التفاعل كيف يطير!\n"
            "تذكر: التفاعل بصدق يعني ترند حقيقي.\n"
            "اضغط إضافة رابطك أولاً، ثم ابدأ التبادل!"
        )
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("➕ إضافة رابط حسابي", callback_data='add_link'))
        markup.add(telebot.types.InlineKeyboardButton("🤝 تبادل (تفاعل كامل)", callback_data='exchange'))
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.data == 'add_link':
            bot.send_message(call.message.chat.id, "أرسل رابط فيديو التيك توك الخاص بك الآن، وسأحفظه في الطابور!")
            
        elif call.data == 'exchange':
            bot.send_message(call.message.chat.id, 
                "🚀 خطة التفاعل السريع:\n"
                "1. ادخل الرابط اللي بيظهر لك.\n"
                "2. تفاعل مع أول 3 فيديوهات (لايك + تعليق + إكسبلور).\n"
                "3. ارجع هنا واضغط 'تم التفاعل' عشان نثبت حقك!")

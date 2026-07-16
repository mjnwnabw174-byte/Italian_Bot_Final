import telebot
import logic
from config import MY_ID

def bot_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        logic.log_to_sheets(user.first_name, user.username or "لا يوجد", "انضم للبوت")
        
        # إشعار للمطور
        try:
            bot.send_message(MY_ID, f"🟢 انضمام: {user.first_name} (@{user.username})")
        except: pass
        
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("➕ إضافة رابط حسابي", callback_data='add_link'))
        markup.add(telebot.types.InlineKeyboardButton("🤝 تبادل (تفاعل كامل)", callback_data='exchange'))
        
        welcome_text = "🔥 أهلاً بك في جيش إيطالي! اختر تكتيكك من الأزرار:"
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        # هنا فصلنا الأزرار عن بعضها
        if call.data == 'add_link':
            bot.answer_callback_query(call.id, "جاهز لحفظ رابطك...")
            bot.send_message(call.message.chat.id, "أرسل رابط فيديو التيك توك الآن:")
            
        elif call.data == 'exchange':
            bot.answer_callback_query(call.id, "جارٍ تجهيز التفاعل...")
            bot.send_message(call.message.chat.id, 
                "🚀 خطة التفاعل السريع:\n"
                "1. ادخل الرابط اللي بيظهر لك.\n"
                "2. تفاعل مع أول 3 فيديوهات (لايك + تعليق + إكسبلور).\n"
                "3. ارجع هنا واضغط 'تم التفاعل'!")

    # هذا الجزء لاستقبال الروابط إذا أرسلها المستخدم كرسالة نصية
    @bot.message_handler(func=lambda message: True)
    def handle_links(message):
        if "tiktok.com" in message.text:
            logic.add_user_to_sheet(message.from_user.username, message.text)
            bot.reply_to(message, "✅ تم حفظ رابطك بنجاح في طابور التبادل!")
        else:
            bot.reply_to(message, "أنا لا أفهم هذا الأمر. استخدم الأزرار يا بطل!")

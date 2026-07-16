import telebot
import logic

def bot_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        # تسجيل الدخول في المخ (Google Sheets)
        logic.log_to_sheets(user.first_name, user.username or "لا يوجد", "انضم للبوت")
        
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
            # هنا ستضيف لاحقاً منطق حفظ الرابط في logic.py
            
        elif call.data == 'exchange':
            # التحقق من وجود رابط (سوف نربطه لاحقاً بـ logic.check_user)
            bot.send_message(call.message.chat.id, 
                "🚀 خطة التفاعل السريع:\n"
                "1. ادخل الرابط اللي بيظهر لك.\n"
                "2. تفاعل مع أول 3 فيديوهات (لايك + تعليق + إكسبلور).\n"
                "3. ارجع هنا واضغط 'تم التفاعل' عشان نثبت حقك!")

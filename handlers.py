import telebot
from config import MY_ID

def bot_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        user_name = message.from_user.username or "مستخدم"
        # إشعار دخول عضو جديد
        bot.send_message(MY_ID, f"🚨 عضو جديد دخل البوت: @{user_name}")
        
        welcome_text = (
            "🔥 أهلاً بك في جيش التفاعل! 🔥\n\n"
            "أنت الآن في المكان الصحيح لتصبح الأفضل.\n"
            "قاعدتنا بسيطة: تفاعل بصدق، يأتيك التفاعل من الجميع.\n"
            "إذا تفاعلت مع 10، نضمن لك تفاعل 100!\n"
            "نحن لا نلعب، نحن نصنع الترند.\n"
            "تفاعل، شارك، وكن القائد!\n"
            "الآن، اختر من الأزرار وابدأ التكتيك."
        )
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("🤝 تبادل (تفاعل كامل)", callback_data='exchange'))
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.data == 'exchange':
            bot.send_message(call.message.chat.id, "انتظر... يتم تجهيز رابط الشخص التالي في الدور.")

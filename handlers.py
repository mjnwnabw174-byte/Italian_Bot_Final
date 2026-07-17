import telebot
from telebot import types
import logic
from config import MY_ID

def bot_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        # تسجيل دخول المستخدم
        user = message.from_user
        logic.log_to_sheets(user.first_name, user.username or "لا يوجد", "انضم للبوت")
        
        # إنشاء الأزرار بشكل احترافي
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("➕ إضافة رابط حسابي", callback_data='add_link')
        btn2 = types.InlineKeyboardButton("🤝 تبادل (تفاعل كامل)", callback_data='exchange')
        btn3 = types.InlineKeyboardButton("📢 شارك البوت لأصدقائك", callback_data='share_bot')
        markup.add(btn1, btn2, btn3)
        
        welcome_text = (
            "🔥 **أهلاً بك يا بطل في جيش إيطالي!**\n\n"
            "نحن هنا لزيادة التفاعل الحقيقي.\n"
            "اختر التكتيك المناسب وابدأ رحلة الصعود! 🚀"
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        # زر إضافة الرابط
        if call.data == 'add_link':
            bot.edit_message_text("أرسل رابط فيديو التيك توك الآن ليتم إضافته للنظام:", call.message.chat.id, call.message.message_id)
        
        # زر التبادل
        elif call.data == 'exchange':
            text = (
                "🚀 **خطة التفاعل السريع:**\n"
                "1. ادخل الرابط اللي بيظهر لك.\n"
                "2. تفاعل مع أول 3 فيديوهات (لايك + تعليق + إكسبلور).\n"
                "3. ارجع هنا واضغط 'تم التفاعل' عشان نثبت حقك!"
            )
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown')
        
        # زر مشاركة البوت (يوزع رابط بوتك أنت)
        elif call.data == 'share_bot':
            bot_username = bot.get_me().username
            bot_link = f"https://t.me/{bot_username}"
            bot.send_message(call.message.chat.id, f"✅ انشر رابط بوتك الخاص واجلب الأبطال:\n{bot_link}")

    @bot.message_handler(func=lambda message: True)
    def handle_messages(message):
        # معالجة الروابط
        if "tiktok.com" in message.text:
            logic.add_user_to_sheet(message.from_user.username, message.text)
            bot.reply_to(message, "✅ تم حفظ رابطك بنجاح في قاعدة البيانات!")
        else:
            bot.reply_to(message, "أنا لا أفهم هذا الطلب، استخدم الأزرار أعلاه! 😈")

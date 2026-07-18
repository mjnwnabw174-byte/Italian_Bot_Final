import telebot
from telebot import types
import logic
from config import MY_ID

def bot_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        logic.log_to_sheets(user.first_name, user.username or "لا يوجد", "بدء البوت")
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("➕ إضافة رابط حسابي", callback_data='add_link')
        btn2 = types.InlineKeyboardButton("🤝 تبادل (كامل كامل)", callback_data='exchange')
        btn3 = types.InlineKeyboardButton("📤 مشاركة البوت لأصدقائك", callback_data='share_bot')
        markup.add(btn1, btn2, btn3)
        
        welcome_text = "🔥 أهلاً بك في جيش إيطالي! 🔥\n\nنحن هنا لزيادة التفاعل الحقيقي.\nاختر التكنيك المناسب وابدأ رحلة الصعود 🚀"
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.data == 'add_link':
            bot.send_message(call.message.chat.id, "أرسل رابط الفيديو الآن")
            bot.edit_message_text("أرسل رابط الفيديو الذي يتم عليه التفاعل", call.message.chat.id, call.message.message_id)
        
        elif call.data == 'exchange':
            text = "تفضل التعامل مع 3 فيديوهات ثم أرجع\n\n📌 **خطة التفاعل السريع** 🚀\n1. أدخل الرابط الذي يظهر لك.\n2. تفاعل مع أول 3 فيديوهات (لايك + تعليق + إكسبلور).\n3. ارجع هنا واضغط 'تم التفاعل' عشان نثبت حقك ✅"
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown')
            
        elif call.data == 'share_bot':
            bot_username = bot.get_me().username
            bot_link = f"https://t.me/{bot_username}"
            bot.send_message(call.message.chat.id, f"انشر رابط بوتك الخاص: {bot_link}")

    @bot.message_handler(func=lambda message: True)
    def handle_messages(message):
        if "tiktok.com" in message.text:
            logic.add_user_to_sheet(message.from_user.username, message.text)
            bot.reply_to(message, "✅ تم حفظ رابطك. سيتم التفاعل معك في قاعدة البيانات.")
        else:
            bot.reply_to(message, "❌ أنا لا أفهم هذا الطلب، استخدم الأزرار أعلاه.")

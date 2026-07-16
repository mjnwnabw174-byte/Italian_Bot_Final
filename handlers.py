import telebot
import logic
from config import MY_ID

def bot_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        logic.log_to_sheets(user.first_name, user.username or "لا يوجد", "انضم للبوت")
        
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("➕ إضافة رابط حسابي", callback_data='add_link'))
        markup.add(telebot.types.InlineKeyboardButton("🤝 تبادل (تفاعل كامل)", callback_data='exchange'))
        
        bot.send_message(message.chat.id, "🔥 أهلاً بك في جيش إيطالي! اختر تكتيكك:", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.data == 'add_link':
            bot.send_message(call.message.chat.id, "أرسل رابط التيك توك الآن:")
        elif call.data == 'exchange':
            bot.send_message(call.message.chat.id, "خطة التفاعل: تفاعل مع 3 فيديوهات ثم ارجع!")

    @bot.message_handler(func=lambda message: True)
    def handle_messages(message):
        if "tiktok.com" in message.text:
            logic.add_user_to_sheet(message.from_user.username, message.text)
            bot.reply_to(message, "✅ تم حفظ رابطك!")

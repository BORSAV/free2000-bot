import telebot
from telebot import types

# BOT SETTINGS
BOT_TOKEN = '7213574149:AAH8Cp2kRBkiDtU3JsINM_vN0WjuJlgdHk4'
CHANNEL_1 = '@frggix'
CHANNEL_2 = '@fraggix_chat'
FOLDER_LINK = 'https://t.me/addlist/urrFsU_GOpsyZGRl'

bot = telebot.TeleBot(BOT_TOKEN)
user_upi = {}

# Check if user is member of both channels
def is_member(chat_id, user_id):
    try:
        status1 = bot.get_chat_member(CHANNEL_1, user_id).status
        status2 = bot.get_chat_member(CHANNEL_2, user_id).status
        return status1 in ['member', 'administrator', 'creator'] and status2 in ['member', 'administrator', 'creator']
    except:
        return False

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Welcome! Enter your UPI ID to claim ₹2000:")
    bot.register_next_step_handler(message, get_upi)

# Get UPI ID and show buttons
def get_upi(message):
    upi = message.text.strip()
    user_upi[message.chat.id] = upi

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔗 Join Channel 1", url="https://t.me/frggix"))
    markup.add(types.InlineKeyboardButton("🔗 Join Channel 2", url="https://t.me/fraggix_chat"))
    markup.add(types.InlineKeyboardButton("📁 Save Folder", url=FOLDER_LINK))
    markup.add(types.InlineKeyboardButton("✅ Done", callback_data='done'))

    bot.send_message(message.chat.id,
                     "✅ Step 2: Join both channels and save the folder, then press ✅ Done.",
                     reply_markup=markup)

# Handle Done button
@bot.callback_query_handler(func=lambda call: call.data == 'done')
def check_done(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    if is_member(chat_id, user_id):
        upi = user_upi.get(chat_id, "Not provided")
        bot.send_message(chat_id, f"🎉 Thank you!\nYour ₹2000 will be created and sent to your UPI ID ({upi}) within 24 hours.")
    else:
        bot.send_message(chat_id, "⚠️ You haven't joined both channels. Please join them and try again.")

# Start polling
bot.infinity_polling()


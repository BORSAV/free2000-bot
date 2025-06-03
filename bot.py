import telebot
from telebot import types

BOT_TOKEN = '7213574149:AAH8Cp2kRBkiDtU3JsINM_vN0WjuJlgdHk4'
CHANNEL_1 = '@frggix'
CHANNEL_2 = '@fraggix_chat'
FOLDER_LINK = 'https://t.me/addlist/urrFsU_GOpsyZGRl'

bot = telebot.TeleBot(BOT_TOKEN)
user_upi = {}

def is_member(chat_id, user_id):
    try:
        status1 = bot.get_chat_member(CHANNEL_1, user_id).status
        status2 = bot.get_chat_member(CHANNEL_2, user_id).status
        return status1 in ['member', 'administrator', 'creator'] and status2 in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Welcome! Enter your UPI ID to claim ₹2000:")
    bot.register_next_step_handler(message, get_upi)

def get_upi(message):
    upi = message.text.strip()
    user_upi[message.chat.id] = upi

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔗 Join Channel 1", url="https

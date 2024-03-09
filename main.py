# Слито в https://t.me/HACKER_PHONE_VIP

import telebot
from telebot import types
import requests
import random
from config import TOKEN, ADMIN
from buttons import glawnaya, otm
bot = telebot.TeleBot(TOKEN)

# Слито в https://t.me/HACKER_PHONE_VIP

@bot.message_handler(commands=['start'])
def welcome(message):
    stickers = ['CAACAgIAAxkBAAEEQDZiO6LQ1D9YIKDdvHKFBRcBXBEwygACkgEAAladvQqf0C0IQi7VBSME','CAACAgIAAxkBAAEEQDRiO6KxBkF-s6dYa4Gw-ArWyik5oAAC9wEAAhZCawo59nBvtGN_xCME','CAACAgIAAxkBAAEEQDJiO6Kk6vt7ojC3w0X7vyUIRnA3jQACBQADwDZPE_lqX5qCa011IwQ','CAACAgIAAxkBAAEEQDBiO6Kdpk8iWtkfWundOeMtyubotQAC5AEAAhZCawqJ5pAaeMCqQSME','CAACAgIAAxkBAAEEQC5iO6KYbeAmrhHbKdlGWgy3VJh35gACAQEAAladvQoivp8OuMLmNCME','CAACAgIAAxkBAAEEQCxiO6KU0deGBfOCDtmhltzQDH9iVgACWg8AAsFkiUtoBn1ASv7hiCME','CAACAgIAAxkBAAEEQCliO6KJKkaBk7qID8WsyLT4tRHQuQAC_wIAAm2wQgMEoDmrNAI2NyME','CAACAgIAAxkBAAEEQChiO6KHDE12zrSz6pKe1Hxb7x4KJQACHQADO3EfIqmCmmAwV9EZIwQ']
    bot.send_sticker(message.chat.id,random.choice(stickers))
    bot.send_message(message.chat.id, f"👋🏻<b> Привет <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!</b>", reply_markup=glawnaya(), parse_mode='HTML')

# Слито в https://t.me/HACKER_PHONE_VIP

@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == "☘️ Администрация":
        markup = types.InlineKeyboardMarkup()
        q = types.InlineKeyboardButton('☘️ Связь с админом', url='https://t.me/' + ADMIN)
        markup.add(q)
        bot.send_message(message.chat.id, "<b>📌 Если у Вас возникли какие либо вопросы, то обратитесь к Администрации!</b>", reply_markup=markup, parse_mode='html')
    elif message.text == '♣️ Профиль':
        markup = types.InlineKeyboardMarkup()
        q0 = types.InlineKeyboardButton(text = "🏴‍☠ Наши проекты", url = f't.me/HPV_HOME')
        markup.add(q0)
        bot.send_message(message.chat.id, f"""<b>⛩ Ваш личный кабинет ⛩
➖➖➖➖➖➖➖➖➖➖
🖍 Ваше имя:</b> <code>{message.from_user.first_name}</code>
<b>——————————
🌀 Ваш юзер: @{message.from_user.username}
——————————
🆔 Ваш Telegram ID:</b> <code>{message.from_user.id}</code>""",parse_mode="HTML", reply_markup=markup)
    elif message.text == "🔎 Поиск по IP":
        bot.send_message(message.chat.id, '<b><b>📍 Введите IP-адрес для получения информации!</b></b>', reply_markup=otm(), parse_mode="HTML")
        bot.register_next_step_handler(message, text)
    elif message.text == "Назад ↩️⁤":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись в главное меню!</b>', reply_markup=glawnaya(), parse_mode='html')

# Слито в https://t.me/HACKER_PHONE_VIP

def text(message):
    if message.text == "Назад ↩️⁤":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись в главное меню!</b>', reply_markup=glawnaya(), parse_mode='html')
    else:
        try:
            ipp = message.text
            q = bot.send_message(message.chat.id, "✅ <b>Ищу информацию, подождите несколько секунд!</b>", parse_mode='html')
            url = 'https://ipwhois.app/json/' + ipp
            json = requests.get(url).json()
            bot.delete_message(message.chat.id, q.message_id)
            bot.send_message(message.chat.id, f'''📌 <b>Информация по IP-адресу:</b> <code>{json["ip"]}</code>
➖➖➖➖➖➖➖➖➖➖
<b>Страна:</b> <code>{json["country"]}</code>
<b>Код страна:</b> <code>{json["country_code"]}</code>
<b>Город:</b> <code>{json["city"]}</code>
<b>Регион:</b> <code>{json["region"]}</code>
➖➖➖➖➖➖➖➖➖➖
<b>Код номера:</b> <code>{json["country_phone"]}</code>
<b>Часовой пояс:</b> <code>{json["timezone_gmt"]}</code>
<b>Валюта:</b> <code>{json["currency_symbol"]}</code>
<b>Знак валюты:</b> <code>{json["currency_code"]}</code>
<b>Провайдер:</b> <code>{json["org"]}</code>
➖➖➖➖➖➖➖➖➖➖
<b>Широта:</b> <code>{json["latitude"]}</code>
<b>Долгота:</b> <code>{json["longitude"]}</code>
➖➖➖➖➖➖➖➖➖➖''', parse_mode='html'
)
            bot.register_next_step_handler(message, text)
        except:
            bot.send_message(message.chat.id, '❌ <b>Неверный IP-адрес или произошла ошибка! Попробуйте попытку!</b>', parse_mode='html')
            bot.register_next_step_handler(message, text)

# Слито в https://t.me/HACKER_PHONE_VIP

while True:
    try:
        bot.polling()
    except:
        continue

# Слито в https://t.me/HACKER_PHONE_VIP
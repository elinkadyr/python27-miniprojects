import telebot
from decouple import config

token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBV5kBYbBYfkDe4MRR3OrfCBv1zYV1QAC7RwAAiZXOUimVQABTfB2UVsuBA'
no_sticker = 'CAACAgIAAxkBAAEIBYFkBYbfcAWv3IPArYLHpL8nzux58QAC2SQAAphN8ElCBpJ0uIjNdy4E'

# клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Yes', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('No', callback_data='no')
keyboard.add(b1, b2)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hi, choose the button', reply_markup=keyboard)

#func - функция фильтр, в данном случае возвращаются все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)

bot.polling()
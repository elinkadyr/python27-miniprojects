import telebot
from decouple import config

token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBV5kBYbBYfkDe4MRR3OrfCBv1zYV1QAC7RwAAiZXOUimVQABTfB2UVsuBA'
no_sticker = 'CAACAgIAAxkBAAEIBYFkBYbfcAWv3IPArYLHpL8nzux58QAC2SQAAphN8ElCBpJ0uIjNdy4E'

bot = telebot.TeleBot(token)

# клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('YES')
b2 = telebot.types.KeyboardButton('NO')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hi, choose the button', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'YES':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'NO':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'tap the button')
        
    bot.register_next_step_handler(message, reply_to_button)

bot.polling()
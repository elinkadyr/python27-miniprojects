import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBVdkBX_5vTBKyQ6tgmXl_0pc20xapwACeA0AAiKQqEp6qUCDdz5Dki4E')
    # bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/i?id=0a776f321bbccb4440fa7c88fe5c75425a432024-9234735-images-thumbs&n=13')

@bot.message_handler(content_types=['text'])
def abc(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет!')
    else:
        bot.send_message(message.chat.id, 'Сообщение не распознанно')

@bot.message_handler(content_types=['sticker'])
def abcd(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    # bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()

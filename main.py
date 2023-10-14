import telebot
from telebot import types

bot = telebot.TeleBot(token='6600333025:AAFTKA4vFVlFwkXuNzELAmjULBzeKdt2mIo')

@bot.message_handler(func=lambda message: True)
def text_message_handler(message):
    user_id = message.chat.id
    text = message.text
    if str(text).lower() == 'привет':
        bot.send_message(user_id, 'здорово')
    else:
        bot.send_message(user_id, 'как дела?')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    welcome_message = 'Добро пожаловать! Яваш Telegram бот.'
    avilibale_commands = '/start - Начать\n/help - Помощь'
    name = message.from_user.first_name
    bot.send_message(user_id, name + welcome_message +avilibale_commands)

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.chat.id
    help_text = 'Выберите действие:'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Узнать новости')
    button2 = types.KeyboardButton('Узнать погоду')
    button3 = types.KeyboardButton('Узнать мероприятия')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(user_id, help_text, reply_markup=markup)

bot.polling(none_stop=True)



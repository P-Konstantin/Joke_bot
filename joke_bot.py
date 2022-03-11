import telebot
import time


# Создаем бота
bot = telebot.TeleBot('token')


# Загружаем список шуток
f = open('data/jokes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()


# Функция, обрабытывающая команду /start
@bot.message_handler(commands=['start'])
def start(message, res=False):
    try:
        # Пока не закончатся шутки, выводим их 
        for joke in jokes:
            bot.send_message(message.chat.id, joke)
            # Делаем паузу
            time.sleep(5)
    except Exception as e:
        bot.send_message(message.chat.id, 'Анекдоты закончились :-(')


# Запускаем бота
bot.polling(none_stop=True, interval=0)

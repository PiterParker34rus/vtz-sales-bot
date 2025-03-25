import telebot
from flask import Flask
import threading

# Укажите свой токен бота
TOKEN = "7719119719:AAEGdxBBBeg8_HlatNBHaf6rk9DrPg_Ra4o"
bot = telebot.TeleBot(TOKEN)

# Запуск мини-вебсервера для поддержки работы через UptimeRobot
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добрый день. Я виртуальный ассистент коммерческого отдела АО \"ВТЗ\". "
                                     "Вы можете получить информацию о непрофильной продукции Волжского трубного завода. "
                                     "Для просмотра всех доступных команд отправьте /commands")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "С полным перечнем непрофильной продукции Вы можете ознакомиться на Портале: "
                                      "https://stock.tmk-group.com")

# Обработчик команды /menu
@bot.message_handler(commands=['menu'])
def send_menu(message):
    menu_text = "Меню:\n"
    menu_text += "1. Непрофильная продукция на АВИТО: "
    menu_text += "https://www.avito.ru/volgogradskaya_oblast_volzhskiy/gruzoviki_i_spetstehnika/pritsep_traktornyy_sarmat_3pts15_2006_7256745627\n"
    menu_text += "2. Связаться с начальником коммерческого отдела по телефону: +788443 55 11 16"
    bot.send_message(message.chat.id, menu_text)

# Обработчик команды /commands (вывод всех доступных команд)
@bot.message_handler(commands=['commands'])
def send_commands(message):
    commands_text = "Доступные команды:\n"
    commands_text += "/start - Приветственное сообщение\n"
    commands_text += "/help - Информация о Портале непрофильной продукции\n"
    commands_text += "/menu - Просмотр продукции на Авито и контакт начальника коммерческого отдела\n"
    bot.send_message(message.chat.id, commands_text)

# Запускаем Flask в отдельном потоке
threading.Thread(target=run_flask).start()

# Запуск бота
bot.polling(none_stop=True)

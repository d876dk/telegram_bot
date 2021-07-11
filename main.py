import config
import telebot
from scripts import insert_users
from scripts import is_admin
from keyboards import main_keyboard, admin_keyboard

bot = telebot.TeleBot(config.TOKEN)


# отправка клавиатуры
@bot.message_handler(commands=['start'])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message.from_user)
    insert_users(user_id=message.from_user.id, first_name=message.from_user.first_name, \
                 last_name=message.from_user.last_name, username=message.from_user.username)
    if is_admin(user_id=message.from_user.id):
        bot.send_message(message.chat.id, 'Привет, ты админ мне /start', reply_markup=admin_keyboard)
    else:
        bot.send_message(message.chat.id, 'Привет, ты никто мне /start', reply_markup=main_keyboard)


@bot.message_handler(content_types=["text"])
def message_processing(message):
    if message.text == "Добавить товар":
        pass
    elif message.text == 'Выбрать категорию':
        pass
    elif message.text == 'Выбрать товары':
        pass
    elif message.text == 'Корзина':
        pass
    elif message.text == "Добавить категорию":
        pass
    elif message.text == "Добавить товар":
        pass
    else:
        bot.send_message(message.chat.id, 'Я не понял вашу команду')


if __name__ == '__main__':
    bot.infinity_polling()

import config
import telebot
from scripts import insert_users
from scripts import is_admin

bot = telebot.TeleBot(config.TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока', 'хех', 'отправь картинку')


# отправка клавиатуры
@bot.message_handler(commands=['start'])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message.from_user)
    insert_users(user_id=message.from_user.id, first_name=message.from_user.first_name, \
                 last_name=message.from_user.last_name, username=message.from_user.username)
    if is_admin(user_id=message.from_user.id):
        keyboard1.row('Добавить категорию', 'Добавить товар')
        bot.send_message(message.chat.id, 'Привет, ты админ мне /start', reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, 'Привет, ты никто мне /start', reply_markup=keyboard1)


if __name__ == '__main__':
    bot.infinity_polling()

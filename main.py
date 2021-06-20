import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока', 'хех', 'отправь картинку')

# отправка клавиатуры
@bot.message_handler(commands=['start'], content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


if __name__ == '__main__':
     bot.infinity_polling()
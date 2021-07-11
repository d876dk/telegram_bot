import telebot

main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
main_keyboard.row('Привет', 'Пока', 'хех', 'отправь картинку')

admin_keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
admin_keyboard.row('Привет', 'Пока', 'хех', 'отправь картинку')
admin_keyboard.row("Добавить категорию", "Добавить товар")


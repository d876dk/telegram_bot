import telebot

main_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
main_keyboard.row('Выбрать категорию', 'Выбрать товары', 'Корзина')

admin_keyboard = telebot.types.ReplyKeyboardMarkup(True,False)
admin_keyboard.row('Выбрать категорию', 'Выбрать товары', 'Корзина')
admin_keyboard.row("Добавить категорию", "Добавить товар")





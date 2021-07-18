import telebot

main_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
main_keyboard.row('Выбрать категорию', 'Выбрать товары', 'Корзина')

admin_keyboard = telebot.types.ReplyKeyboardMarkup(True,False)
admin_keyboard.row('Выбрать категорию', 'Выбрать товары', 'Корзина')
admin_keyboard.row("Добавить категорию", "Добавить товар")

agreement_keyboard =  telebot.types.InlineKeyboardMarkup()
agreement_keyboard.width = 2
agreement_keyboard.add(telebot.types.InlineKeyboardButton("Да", callback_data="agreement_yes"),telebot.types.InlineKeyboardButton("Нет", callback_data="agreement_no"))


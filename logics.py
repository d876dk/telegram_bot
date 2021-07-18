import telebot
from scripts import add_category_to_db, get_category


def get_category_keyboards():
    data = get_category()
    cat_keyboard = telebot.types.InlineKeyboardMarkup()
    for i in data:
        cat_keyboard.add(telebot.types.InlineKeyboardButton(i[1], callback_data=i[0]))
    cat_keyboard.add(telebot.types.InlineKeyboardButton("Вернуться назад", callback_data="back"))
    return  cat_keyboard

def add_category(status, message):
    if status == "cc0":
        return "Введите название создаваемой категории"
    if status == "cc1":
        try:
            add_category_to_db(message.text.lower())
            return "Категория добавлена успешно"
        except Exception as e:
            return "Ошибка при добавлении категории. Возможно такая категория уже существует"


def add_product(status, message):
    """
    Функция озвращает данные соответсвенно статуа пользователя
    :param status:
    :param message:
    :return:
    """
    if status == "cp0":
        return "Введите название продукта"
    elif status == "cp1":
        return "Введите описание товара"
    elif status == "cp2":
        return "Введите цену товара"
    elif status == "cp3":
        return "Выберите категорию товара из списка"
    elif status == "cp4":
        return "Добавьте изображение товара"

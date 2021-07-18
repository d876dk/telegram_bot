import telebot
from scripts import add_category_to_db


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
    if status == "cp0":
        return "Введите название продукта"
    if status == "cp1":
        product_name = message.text
        return "Выберите категорию продукта"



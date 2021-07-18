import config
import telebot
from scripts import insert_users,is_admin, get_category,get_category_id,add_product_to_db
from keyboards import main_keyboard, admin_keyboard,agreement_keyboard
from logics import add_category, add_product, get_category_keyboards

bot = telebot.TeleBot(config.TOKEN)

users_data = {}


# отправка клавиатуры
@bot.message_handler(commands=['start'])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message.from_user)
    insert_users(user_id=message.from_user.id, first_name=message.from_user.first_name, \
                 last_name=message.from_user.last_name, username=message.from_user.username)
    users_data[message.from_user.id] = {"status": "start"}
    print(users_data)
    if is_admin(user_id=message.from_user.id):
        bot.send_message(message.chat.id, 'Привет, ты админ мне /start', reply_markup=admin_keyboard)
    else:
        bot.send_message(message.chat.id, 'Привет, ты никто мне /start', reply_markup=main_keyboard)


@bot.message_handler(content_types=["text"])
def message_processing(message):
    try:
        if users_data[message.from_user.id]:
            pass
    except KeyError:
        users_data[message.from_user.id] = {"status": "start"}
    if message.text == 'Выбрать категорию':
        pass
    elif message.text == 'Выбрать товары':
        pass
    elif message.text == 'Корзина':
        pass
    elif message.text == "Добавить категорию":
        users_data[message.from_user.id]["status"] = "cc0"
        mes = add_category(users_data[message.from_user.id]["status"], message)
        bot.send_message(message.chat.id, mes, reply_markup=admin_keyboard)
        users_data[message.from_user.id]["status"] = "cc1"

    elif message.text == "Добавить товар":
        users_data[message.from_user.id]["status"] = "cp0"
        mes = add_product(users_data[message.from_user.id]["status"], message)
        bot.send_message(message.chat.id, mes, reply_markup=admin_keyboard)
        users_data[message.from_user.id]["status"] = "cp1"
    elif users_data[message.from_user.id]["status"] == "cp1":
        users_data[message.from_user.id]["name"] = message.text
        mes = add_product(users_data[message.from_user.id]["status"], message)
        bot.send_message(message.chat.id, mes, reply_markup=admin_keyboard)
        users_data[message.from_user.id]["status"] = "cp2"
    elif users_data[message.from_user.id]["status"] == "cp2":
        users_data[message.from_user.id]["desc"] = message.text
        mes = add_product(users_data[message.from_user.id]["status"], message)
        bot.send_message(message.chat.id, mes, reply_markup=admin_keyboard)
        users_data[message.from_user.id]["status"] = "cp3"
    elif users_data[message.from_user.id]["status"] == "cp3":
        users_data[message.from_user.id]["price"] = message.text
        mes = add_product(users_data[message.from_user.id]["status"], message)
        bot.send_message(message.chat.id, mes, reply_markup=get_category_keyboards())

    elif users_data[message.from_user.id]["status"] == "cc1":
        mes = add_category(users_data[message.from_user.id]["status"], message)
        bot.send_message(message.chat.id, mes, reply_markup=admin_keyboard)
        users_data[message.from_user.id]["status"] = "start"
    else:
        bot.send_message(message.chat.id, 'Я не понял вашу команду')


@bot.message_handler(content_types=["photo"])
def product_photo_handler(message):
    if users_data[message.from_user.id]["status"] == "cp4":
        img_info = bot.get_file(message.photo[0].file_id)
        downloaded_file = bot.download_file(img_info.file_path)
        users_data[message.from_user.id]["image"] = downloaded_file
        users_data[message.from_user.id]["status"] = "cp5"
        cat_name = get_category_id(users_data[message.from_user.id]["category_id"])[0]
        bot.send_message(message.chat.id, f"Проврьте правильность введенных данных\n\n"
                                          f"Имя продукта: {users_data[message.from_user.id]['name']}\n"
                                          f"Описание продукта: {users_data[message.from_user.id]['desc']}\n"
                                          f"Цена продукта: {users_data[message.from_user.id]['price']}\n"
                                          f"Описание продукта: {users_data[message.from_user.id]['desc']}\n"
                                          f"Категория продукта: {cat_name}\n")

        bot.send_photo(message.chat.id,users_data[message.from_user.id]['image'])
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=agreement_keyboard)

@bot.callback_query_handler(func=lambda call: True)
def calback_data_handler(call):
    if call.data == "back":
        bot.send_message(call.chat.id, "Выберите категорию товара из списка",
                         reply_markup=get_category_keyboards())
    elif call.data == "agreement_yes":
        add_product_to_db(users_data[call.from_user.id])
    elif call.data == "agreement_no":
        users_data[call.from_user.id]["status"] = "start"
    else:
        users_data[call.from_user.id]["category_id"] = call.data
        users_data[call.from_user.id]["status"] = "cp4"
        mes = add_product(users_data[call.from_user.id]["status"], call)
        bot.send_message(call.from_user.id, mes, reply_markup=admin_keyboard)
    print(users_data)



if __name__ == '__main__':
    bot.infinity_polling()

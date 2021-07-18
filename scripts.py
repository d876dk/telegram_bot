import sqlite3
from config import DB_NAME


def insert_users(user_id, username, first_name, last_name):
    """
    add user in users db
    :param user_id: telgram user id
    :param username:
    :param first_name:
    :param last_name:
    :return: pass
    """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    try:
        cursor.execute("""
        INSERT INTO users  ('user_id','first_name','last_name','username','admin')
        VALUES ( ?,?,?,?,? )
        """, (user_id, first_name, last_name, username, 0))
    except sqlite3.IntegrityError:
        pass
    db.commit()
    db.close()


def is_admin(user_id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM users
        WHERE user_id = ?
    """, (user_id,))
    if cursor.fetchone()[-1] == 1:
        db.close()
        return True
    else:
        db.close()
        return False


def add_category_to_db(name_category):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # cursor.execute("""
    #     INSERT INTO product_categories (category_name,) VALUES (?,)
    # """,(name_category))

    cursor.execute('INSERT INTO product_categories (category_name) VALUES (?)',
                   (name_category,))

    db.commit()
    db.close()


def get_category():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    cursor.execute("""
    SELECT * FROM product_categories 
    """)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def get_category_id(cat_id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("""
        SELECT category_name FROM product_categories 
        WHERE id = ?
        """,(cat_id,))
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data
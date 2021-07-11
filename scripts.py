import sqlite3


def insert_users(user_id, username, first_name, last_name):
    """
    add user in users db
    :param user_id: telgram user id
    :param username:
    :param first_name:
    :param last_name:
    :return: pass
    """
    db = sqlite3.connect("db1.sqlite")
    cursor = db.cursor()
    cursor.execute("""
    INSERT OR IGNORE INTO users  ('user_id','first_name','last_name','username','admin')
    VALUES ( ?,?,?,?,? )
    """, (user_id, first_name, last_name, username,0))
    db.commit()
    db.close()
def is_admin(user_id):
    db = sqlite3.connect("db1.sqlite")
    cursor = db.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE user_id = ?
    """, (user_id,))
    if cursor.fetchall()[0][-1] == 1:
        return True
    else:
        return False
    db.commit()
    db.close()
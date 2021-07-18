import sqlite3
from config import DB_NAME

db = sqlite3.connect(DB_NAME)
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    first_name TEXT, 
    last_name TEXT,
    username TEXT,
    admin BOOLEAN NOT NULL CHECK (admin IN (0, 1))
) 
""")
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    product_description TEXT,
    product_price INTEGER,
    categories_id INTEGER,
     FOREIGN KEY(categories_id) REFERENCES product_categories(id)
     
)
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_categories(
    id INTEGER PRIMARY KEY,
    category_name TEXT UNIQUE
)
""")

# users = [
#     ("asdjd", "asd@gma"),
#     ("asda12jd", "asd@g123ma")
# ]
# name = "Denis"
# email = "d876dk@gmail.com"


# cursor.execute("""
#     SELECT * FROM users
#     WHERE email = ?
# """, (email,))


# cursor.execute("""
#     SELECT * FROM users
#     ORDER BY id DESC
# """)


# cursor.execute("""
#     SELECT * FROM users
#     WHERE email = :email
# """, {'email': email})
# print(cursor.fetchall())
db.commit()
db.close()

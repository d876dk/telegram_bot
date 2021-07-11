import sqlite3

db = sqlite3.connect("db1.sqlite")
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
    categories_id INTEGER,
     FOREIGN KEY(categories_id) REFERENCES product_categories(id)
)
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_categories(
    id INTEGER PRIMARY KEY,
    product_name TEXT
)
""")

# users = [
#     ("asdjd", "asd@gma"),
#     ("asda12jd", "asd@g123ma")
# ]
# name = "Denis"
# email = "d876dk@gmail.com"


cursor.execute("""
INSERT OR IGNORE INTO users ('user_id','first_name','last_name','username','admin')
VALUES ( ?,?,?,?,? )
""", (2, "asdas", "adhdg", "fdffjhasd",1))

cursor.execute("""
INSERT OR IGNORE INTO product_categories ('product_name')
VALUES ( ? )
""", ("фрукты",))


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

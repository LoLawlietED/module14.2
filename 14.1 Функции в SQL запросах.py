import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Users;")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
""")
for info in range(1,11):
    age = info * 10
    balance = 1000
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{info}", f"example{info}@gmail.com", age, balance))
for balances in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, balances))
for delet in range(1, 11, 3):
    cursor.execute(" DELETE FROM Users WHERE id = ?", (delet,))
cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    username, email, age, balance = user
    #print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
id_1 = cursor.fetchone()[0]
print(id_1)
cursor.execute("SELECT SUM(balance) FROM Users")
summa = cursor.fetchone()[0]
print(summa)
cursor.execute("SELECT AVG(balance) FROM Users")
avg = cursor.fetchone()[0]
print(avg)

connection.commit()
connection.close()
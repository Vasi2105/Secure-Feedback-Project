import sqlite3

conn = sqlite3.connect('feedback.db')


cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, message TEXT)')

conn.commit()
conn.close()

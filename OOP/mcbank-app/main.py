import sqlite3

conn = sqlite3.connect("mc-bank.db")

# User accounts table
conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# User transactions table
conn.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_id INTEGER NOT NULL,
        receiver_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert mock user accounts
conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "password1"))
conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "password2"))

# Insert mock transactions
conn.execute("INSERT INTO transactions (sender_id, receiver_id, amount) VALUES (?, ?, ?)", (1, 2, 100.00))

conn.commit()

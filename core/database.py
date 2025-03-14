import sqlite3

def init_db():
    conn = sqlite3.connect('core/omnibot.db')
    c = conn.cursor()
    
    # Table for message logging
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (user_id TEXT, username TEXT, content TEXT, timestamp TEXT, channel_id TEXT)''')

    # Table for user tracking
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id TEXT PRIMARY KEY, username TEXT, join_date TEXT, messages_sent INTEGER DEFAULT 0)''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

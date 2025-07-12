import sqlite3
import os

DB_PATH = os.path.join("data", "preferences.db")

def init_preferences_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY,
            city TEXT,
            email_time TEXT,
            day_of_week TEXT,
            frequency TEXT,
            personality TEXT,
            email_address TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_preferences(city, email_time, day_of_week, frequency, personality, email_address):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM preferences")  # overwrite if single-user
    c.execute("""
        INSERT INTO preferences (city, email_time, day_of_week, frequency, personality, email_address)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (city, email_time.strftime("%H:%M"), day_of_week, frequency, personality, email_address))
    conn.commit()
    conn.close()

def get_preferences():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT city, email_time, day_of_week, frequency, personality, email_address FROM preferences LIMIT 1")
    row = c.fetchone()
    conn.close()
    return row if row else (None, None, None, None, None, None)

import sqlite3
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)
DB_PATH = os.path.join("data", "logs.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT, 
            source TEXT,
            status TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_event(source: str, status: str, message: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().isoformat(timespec="seconds")
    c.execute(
        "INSERT INTO logs (source, status, message, timestamp) VALUES (?, ?, ?, ?)",
        (timestamp, source, status, message)
    )
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows
import sqlite3
import json
from datetime import datetime

DB_FILE = "scan_history.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            timestamp TEXT,
            results TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_scan(target, results):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scans (target, timestamp, results) VALUES (?, ?, ?)",
        (target, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), json.dumps(results, default=str))
    )
    conn.commit()
    conn.close()


def get_all_scans():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, target, timestamp, results FROM scans ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    save_scan("test.com", {"note": "this is a test scan"})
    print(get_all_scans())
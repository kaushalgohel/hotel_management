import sqlite3

def connect_db():
    conn = sqlite3.connect("database/hotel.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT,
            check_in DATE,
            check_out DATE,
            room_number INTEGER
        )
    """)
    conn.commit()
    return conn

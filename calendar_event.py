import sqlite3

class CalendarEvent:
    def __init__(self, title, start_time, end_time, location=None, description=None):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.description = description

    def save_to_db(self, db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                location TEXT,
                description TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO events (title, start_time, end_time, location, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.title, self.start_time, self.end_time, self.location, self.description))
        conn.commit()
        conn.close()

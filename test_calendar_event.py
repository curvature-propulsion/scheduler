import unittest
import sqlite3
from calendar_event import CalendarEvent

class TestCalendarEvent(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_calendar.db'
        self.event = CalendarEvent(
            title='Meeting',
            start_time='2023-03-01 10:00:00',
            end_time='2023-03-01 11:00:00',
            location='Conference Room',
            description='Discuss project updates'
        )

    def tearDown(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS events')
        conn.commit()
        conn.close()

    def test_save_to_db(self):
        self.event.save_to_db(self.db_path)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM events')
        events = cursor.fetchall()
        conn.close()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0][1], 'Meeting')
        self.assertEqual(events[0][2], '2023-03-01 10:00:00')
        self.assertEqual(events[0][3], '2023-03-01 11:00:00')
        self.assertEqual(events[0][4], 'Conference Room')
        self.assertEqual(events[0][5], 'Discuss project updates')

if __name__ == '__main__':
    unittest.main()

import unittest
from calendar_event import CalendarEvent

class TestCalendarEvent(unittest.TestCase):
    def test_event_creation(self):
        event = CalendarEvent("Meeting", "2023-10-10 10:00", "2023-10-10 11:00", "Office", "Discuss project")
        self.assertEqual(event.title, "Meeting")
        self.assertEqual(event.start_time, "2023-10-10 10:00")
        self.assertEqual(event.end_time, "2023-10-10 11:00")
        self.assertEqual(event.location, "Office")
        self.assertEqual(event.description, "Discuss project")

if __name__ == '__main__':
    unittest.main()

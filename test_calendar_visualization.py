import unittest
from calendar_visualization import print_calendar_today
from io import StringIO
import sys

class TestCalendarVisualization(unittest.TestCase):
    def test_print_calendar_today(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_calendar_today()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Calendar for", output)
        self.assertIn("9:00 AM: Meeting with team", output)
        self.assertIn("11:00 AM: Project discussion", output)
        self.assertIn("1:00 PM: Lunch break", output)
        self.assertIn("3:00 PM: Code review", output)
        self.assertIn("5:00 PM: Wrap up", output)

if __name__ == '__main__':
    unittest.main()

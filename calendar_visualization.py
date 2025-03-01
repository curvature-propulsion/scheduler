from datetime import datetime

def print_calendar_today():
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"Calendar for {today}:")
    print("- 9:00 AM: Meeting with team")
    print("- 11:00 AM: Project discussion")
    print("- 1:00 PM: Lunch break")
    print("- 3:00 PM: Code review")
    print("- 5:00 PM: Wrap up")

if __name__ == "__main__":
    print_calendar_today()

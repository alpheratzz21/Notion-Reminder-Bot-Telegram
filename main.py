# File: main.py

from get_reminder_data import get_upcoming_reminders
import json

# Load mapping dari config.json
with open("config/config.json") as f:
    config = json.load(f)

column_mapping = config["column_mapping"]

def main():
    reminders = get_upcoming_reminders()
    for item in reminders:
        task = item.get("title", "No Title")
        due = item.get("date", "No Date")
        status = item.get("status", "Unknown")
        print(f"🔔 {task} → {due} (Status: {status})")
if __name__ == "__main__":
    main()

import os
import requests
from get_reminder_data import get_upcoming_reminders
import json

load_dotenv()
TELEGRAM_TOKEN = os.environ("TELEGRAM_TOKEN")
CHAT_ID = os.environ("TELEGRAM_CHAT_ID")

with open("config/config.json") as f:
    config = json.load(f)
column_mapping = config["column_mapping"]

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)

def main():
    reminders = get_upcoming_reminders()
    for item in reminders:
        task = item.get("title", "No Title")
        due = item.get("date", "No Date")
        status = item.get("status", "No Status")

        send_telegram_message(f"📌 {task}\n📅 Deadline: {due}\n🔖 Status: {status}")

if __name__ == "__main__":
    main()

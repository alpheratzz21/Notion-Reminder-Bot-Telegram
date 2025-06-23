from get_reminder_data import get_upcoming_reminders
import json
import os
import requests

# Load env direct from GitHub Actions
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "").strip()
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()

# Load mapping from config.json
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
        status = item.get("status", "Unknown")
        desc = item.get("description", "")

        message = f"📌 {task}\n📅 Deadline: {due}\n🔖 Status: {status} \n 📝 Deskripsi :{desc} "
        print(message)
        send_telegram_message(message)

if __name__ == "__main__":
    main()

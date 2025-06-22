import os
import datetime
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from get_reminder_data import get_upcoming_reminders
import json

# Load config
with open("config/config.json") as f:
    config = json.load(f)

column_mapping = config["column_mapping"]

SCOPES = ['https://www.googleapis.com/auth/calendar']

def google_login():
    creds_json = os.getenv("GOOGLE_CALENDAR_CREDENTIALS")
    print("[DEBUG] creds_json exists:", bool(creds_json))
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    return build("calendar", "v3", credentials=creds)

def main():
    service = google_login()
    reminders = get_upcoming_reminders()

    for item in reminders:
        task = item.get(column_mapping["title"], "No Title")
        date_str = item.get(column_mapping["date"], None)
        if not date_str:
            continue

        date = datetime.datetime.fromisoformat(date_str).date()
        event = {
            'summary': task,
            'start': {'date': date.isoformat()},
            'end': {'date': (date + datetime.timedelta(days=1)).isoformat()},
        }

        service.events().insert(calendarId='primary', body=event).execute()
        print(f"✅ Synced: {task} → {date}")

if __name__ == '__main__':
    main()

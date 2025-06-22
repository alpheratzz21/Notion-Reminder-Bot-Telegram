import os
import datetime
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from get_reminder_data import get_upcoming_reminders
import json

# Load config
with open("config/config.json") as f:
    config = json.load(f)

column_mapping = config["column_mapping"]

# Jika ubah lingkup, hapus token.json
SCOPES = ['https://www.googleapis.com/auth/calendar']

def google_login():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            from google.oauth2.service_account import Credentials
            import json
            import os

            def google_login():
                creds_json = os.getenv("GOOGLE_CALENDAR_CREDENTIALS")
                creds_dict = json.loads(creds_json)
                creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
                return build("calendar", "v3", credentials=creds)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

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

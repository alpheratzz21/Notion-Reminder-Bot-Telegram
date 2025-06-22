# 🧠 Notion Reminder Bot → Telegram 📅📬

Automatically fetch reminders from your Notion database and send them directly to Telegram. No need to open Notion daily — it runs automatically via GitHub Actions.

---

## ✨ Features

- 🔄 Syncs with Notion database
- 📬 Sends personal daily reminders via Telegram
- 🕒 Runs on schedule using GitHub Actions
- ⚙️ Easy configuration via `config.json`
- ✅ Filters out tasks marked as “done”
- 🔐 Uses Notion API & Telegram Bot API

---

## 🧱 Project Structure

.
├── config/
│└── config.json
├── get_reminder_data.py # Fetches data from Notion
├── send_telegram_reminder.py # Sends message to Telegram
├── main.py # Entry point, combines logic
├── .env # (Optional for local development)
└── .github/workflows/main.yml # GitHub Actions workflow

---

## ⚙️ Setup Instructions

### 1. 🔑 Create GitHub Action Secrets

| Secret Name         | Description |
|---------------------|-------------|
| `NOTION_SECRET`     | Notion API token from [Notion Integrations](https://www.notion.so/my-integrations) |
| `TELEGRAM_TOKEN`    | Token from your bot via [BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID`  | Your Telegram chat ID (obtain via sending message to the bot, then calling `getUpdates`) |

Add these via **GitHub → Settings → Secrets → Actions**.

---

### 2. 🗃️ Configure `config/config.json`

json
{
  "database_id": "YOUR_NOTION_DATABASE_ID",
  "column_mapping": {
    "title": "Title",
    "date": "Date",
    "status": "Status",
  }
}

##🚀 How It Works
get_reminder_data.py: Queries Notion for tasks with date ≥ today and status ≠ "done"

send_telegram_reminder.py: Sends those tasks to Telegram

main.py: Runs both scripts together

.github/workflows/main.yml: Automates the execution daily via GitHub Actions

##🧪 Optional Local Testing
Create a .env file:
NOTION_SECRET=your_secret
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
Then run:
pip install -r requirements.txt
python main.py

##📆 GitHub Actions Automation
Already includes a scheduler in main.yml:
on:
  schedule:
    - cron: '0 23 * * *' # Every Day 06:00 AM GMT+7
  workflow_dispatch:

##🧩 Technical Notes
Uses a combination of filters: checkbox = true and date >= today

Tasks with "status": "done" are excluded

Your Telegram bot must have interacted with the target chat at least once

##📥 Credits & Acknowledgments
Notion SDK for Python

Telegram Bot API

GitHub Actions

Assisted by AI tools including ChatGPT 🤖

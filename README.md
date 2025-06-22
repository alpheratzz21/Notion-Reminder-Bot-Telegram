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
│ └── config.json
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

```json

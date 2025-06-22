from notion_client import Client
import os
import datetime
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load config.json
with open("config/config.json") as f:
    config = json.load(f)

column_mapping = config["column_mapping"]
DATABASE_ID = config["database_id"]

notion = Client(auth=os.environ["NOTION_SECRET"])

def format_property(prop):

    if prop["type"] == "title":
        return prop["title"][0]["plain_text"] if prop["title"] else ""
    elif prop["type"] == "rich_text":
        return prop["rich_text"][0]["plain_text"] if prop["rich_text"] else ""
    elif prop["type"] == "date":
        return prop["date"]["start"] if prop["date"] else ""
    elif prop["type"] == "checkbox":
        return prop["checkbox"]
    elif prop["type"] == "select":
        return prop["select"]["name"] if prop["select"] else ""
    elif prop["type"] == "status":
        return prop["status"]["name"] if prop["status"] else ""
    elif prop["type"] == "number":
        return prop["number"]
    elif prop["type"] == "multi_select":
        return [i["name"] for i in prop["multi_select"]]
    elif prop["type"] == "people":
        return [i["name"] for i in prop["people"]]
    else:
        return str(prop.get(prop["type"], ""))


def get_upcoming_reminders():
    today = datetime.datetime.now().isoformat()

    filters = []
    if "reminder" in column_mapping:
        filters.append({
            "property": column_mapping["reminder"],
            "checkbox": {"equals": True}
        })
    if "date" in column_mapping:
        filters.append({
            "property": column_mapping["date"],
            "date": {"on_or_after": today}
        })

    query = notion.databases.query(
        database_id=DATABASE_ID,
        filter={"and": filters}
    )

    results = []
    for page in query["results"]:
        props = page["properties"]
        formatted = {
            field_alias: format_property(props[notion_name])
            for field_alias, notion_name in column_mapping.items()
            if notion_name in props
        }

        status = formatted.get("status", "").lower()
        if status == "done":
            continue

        results.append(formatted)

    results.sort(key=lambda x: x.get("date"))

    return results

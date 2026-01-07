import requests
import os
from datetime import datetime
from pathlib import Path

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://net.schoolbuscity.com"
STATE_FILE = "alerted_today.txt"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

today = datetime.now().strftime("%Y-%m-%d")

# Check if we already alerted today
if Path(STATE_FILE).exists():
    if Path(STATE_FILE).read_text().strip() == today:
        print("Already alerted today. Exiting.")
        exit()

page = requests.get(URL, timeout=10).text.lower()

# STRONGER condition (not just any 'cancel')
if "transportation has been cancelled" in page or "buses are cancelled" in page:
    send_message("🚨 SCHOOL BUS SERVICE IS CANCELLED TODAY")
    Path(STATE_FILE).write_text(today)
else:
    print("Buses running. No alert.")

import requests
import os
from datetime import datetime
import pytz

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://net.schoolbuscity.com"

# Toronto timezone
tz = pytz.timezone("America/Toronto")
now = datetime.now(tz)

# Time window: 5:30 AM – 8:45 AM
start = now.replace(hour=5, minute=30, second=0)
end = now.replace(hour=8, minute=45, second=0)

if not (start <= now <= end):
    print("Outside checking window. Exiting.")
    exit()

def send_message(text):
    api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(api, data={
        "chat_id": CHAT_ID,
        "text": text
    })

page = requests.get(URL, timeout=10).text.lower()

if "cancel" in page or "closed" in page:
    send_message("🚨 SCHOOL BUS SERVICE IS CANCELLED TODAY")
else:
    print("No cancellation detected.")

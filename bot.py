import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://net.schoolbuscity.com"

def send_message(text):
    api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(api, data={
        "chat_id": CHAT_ID,
        "text": text
    })

response = requests.get(URL, timeout=10)
content = response.text.lower()

if "cancel" in content or "closed" in content:
    send_message("🚨 School bus service is CANCELLED today!")
else:
    print("No cancellation detected.")

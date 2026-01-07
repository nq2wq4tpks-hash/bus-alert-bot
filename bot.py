{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tqdec\tx52\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
from bs4 import BeautifulSoup\
import time\
import os\
\
BOT_TOKEN = os.getenv("BOT_TOKEN")\
CHAT_ID = os.getenv("CHAT_ID")\
\
URL = "https://net.schoolbuscity.com"\
alert_sent = False\
\
def send_message(msg):\
    requests.get(\
        f"https://api.telegram.org/bot\{BOT_TOKEN\}/sendMessage",\
        params=\{"chat_id": CHAT_ID, "text": msg\}\
    )\
\
def check_site():\
    global alert_sent\
    r = requests.get(URL, timeout=10)\
    text = r.text.lower()\
\
    if "cancelled" in text and not alert_sent:\
        send_message("\uc0\u55357 \u57000  SCHOOL BUSES ARE CANCELLED TODAY")\
        alert_sent = True\
\
    if "cancelled" not in text:\
        alert_sent = False\
\
while True:\
    check_site()\
    time.sleep(900)}
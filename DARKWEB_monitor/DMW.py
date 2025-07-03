# DWM-IN-Everywhere: Dark Web Monitoring Everywhere
# Credential Scanning | Breach Notification | Threat Intelligence | Real-Time Monitoring
# Author: Purushotham

import os
import requests
import json
import time
import threading
from datetime import datetime
from pymongo import MongoClient

# Load Environment Variables
HIBP_API_KEY = os.getenv('HIBP_API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# MongoDB Setup
client = MongoClient('mongodb://localhost:27017/')
db = client['dwm_everywhere']
collection = db['breach_reports']

# Telegram Notification
def send_telegram_notification(message):
    if TELEGRAM_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        try:
            requests.post(url, data=payload, timeout=10)
        except Exception as e:
            print(f"[!] Telegram notification failed: {e}")

# Credential Breach Check
def check_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": HIBP_API_KEY, "user-agent": "dwm-everywhere-script"}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            breaches = response.json()
            for breach in breaches:
                record = {
                    "email": email,
                    "title": breach['Title'],
                    "domain": breach['Domain'],
                    "breach_date": breach['BreachDate'],
                    "added_date": datetime.now()
                }
                collection.insert_one(record)
                message = f"⚠️ Breach Alert:\nEmail: {email}\nBreach: {breach['Title']}\nDomain: {breach['Domain']}\nDate: {breach['BreachDate']}"
                print(message)
                send_telegram_notification(message)
        elif response.status_code == 404:
            print(f"[✔️] No breach found for {email}.")
        else:
            print(f"[!] API error: {response.status_code}")
    except Exception as e:
        print(f"[!] Exception during breach check: {e}")

# Simulated Threat Intelligence Fetch
def fetch_threat_intel():
    print(f"[+] Simulating threat intelligence fetch at {datetime.now()}")
    # Extend with real threat feed parsing in advanced phase

# Monitoring Loop
def monitor_emails(email_list, interval=3600):
    while True:
        print(f"[🔍] Scan started at {datetime.now()}")
        for email in email_list:
            check_breach(email)
        fetch_threat_intel()
        print(f"[⏱️] Sleeping for {interval} seconds...\n")
        time.sleep(interval)

if __name__ == '__main__':
    emails_to_monitor = [
        "test1@gmail.com",
        "test2@yahoo.com"
    ]
    scan_interval = 3600  # 1 hour
    monitor_thread = threading.Thread(target=monitor_emails, args=(emails_to_monitor, scan_interval))
    monitor_thread.start()
    print("[✅] DWM-IN-Everywhere Started. Monitoring for breaches and threats...")

# 🕸️ DWM-IN-Everywhere

![Linux Tested](https://img.shields.io/badge/Linux-Tested-green?logo=linux)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-Supported-brightgreen?logo=mongodb)
![Telegram Notifications](https://img.shields.io/badge/Notifications-Telegram-blue?logo=telegram)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

🚀 **Dark Web Monitoring Everywhere (Linux Edition)**

A **cross-platform, lightweight dark web monitoring tool** to help you **track credential breaches, receive instant Telegram alerts, store reports in MongoDB, and learn real cybersecurity workflows practically.**

---

## 🚀 Features

✅ Credential scanning using HaveIBeenPwned (HIBP) API  
✅ Telegram notifications for instant breach alerts  
✅ MongoDB logging for analysis and reporting  
✅ CLI-based, lightweight monitoring  
✅ Linux/Windows compatible  
✅ Expandable with threat intelligence and Tor scraping

---

## ⚙️ Quick Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/purushotham044/DWM.git
cd DWM
2️⃣ Install Dependencies
If your repo has:

requirements.txt:

pip install -r requirements.txt
or setup.sh:

chmod +x setup.sh
./setup.sh
3️⃣ Run the Tool
Check your README or your main Python file:

If it’s main.py:

python main.py
or whatever your startup file is.

4️⃣ Additional Steps (if needed)
If the project uses environment variables (.env), set them:

export VARIABLE=value
If it needs tor for dark web scraping, ensure tor is installed:

sudo apt install tor
and started:

sudo service tor start


# Mini SIEM - Security Log Monitoring & Threat Detection

A beginner-friendly Security Information and Event Management (SIEM) project built using Python, Flask, and SQLite.

This project monitors system logs, detects suspicious behavior, and displays alerts in a web dashboard.

## Features

### 1. Brute Force Detection
Detects repeated failed login attempts from the same IP address.

Rule:
- More than 3 failed login attempts from the same IP

Example:
FAILED_LOGIN admin 192.168.1.20

---

### 2. Port Scan Detection
Detects when a single IP accesses multiple different ports.

Rule:
- 4 or more unique ports accessed by same IP

Example:
PORT_ACCESS 192.168.1.50 22
PORT_ACCESS 192.168.1.50 80
PORT_ACCESS 192.168.1.50 443
PORT_ACCESS 192.168.1.50 3306

---

### 3. Password Spraying Detection
Detects one IP attempting to log into multiple accounts.

Rule:
- 4 or more different usernames targeted by same IP

Example:
FAILED_LOGIN admin 192.168.1.80
FAILED_LOGIN user1 192.168.1.80
FAILED_LOGIN user2 192.168.1.80
FAILED_LOGIN user3 192.168.1.80

---

## Technologies Used

- Python 3
- Flask
- SQLite

---

## Project Structure

mini-siem/
│── app.py
│── log_parser.py
│── detector.py
│── database.py
│── requirements.txt
│── README.md
│── siem.db
│── logs/
│   └── sample.log
│── templates/
│   └── dashboard.html

---

## Installation

Clone repository:

git clone <your-repository-url>

Go to project folder:

cd mini-siem

Install dependencies:

pip install -r requirements.txt

---

## Run Project

Start Flask server:

python app.py

Open browser:

http://127.0.0.1:5000

---

## Supported Log Formats

Login logs:

YYYY-MM-DD HH:MM:SS FAILED_LOGIN username ip

Example:

2026-05-03 09:01:15 FAILED_LOGIN admin 192.168.1.20

Port scan logs:

YYYY-MM-DD HH:MM:SS PORT_ACCESS ip port

Example:

2026-05-03 09:03:00 PORT_ACCESS 192.168.1.50 22

---

## Detection Logic

Brute Force:
- Count failed login attempts per IP
- Alert if count > 3

Port Scan:
- Count unique ports accessed by IP
- Alert if ports >= 4

Password Spraying:
- Count unique usernames attacked by IP
- Alert if usernames >= 4

---

## Dashboard Features

Displays:
- Parsed logs
- Alert type
- IP address
- Number of suspicious events

---

## Future Improvements

- Real-time log monitoring
- Email alerts
- GeoIP lookup
- Threat intelligence integration
- Login authentication
- Charts and analytics
- Export reports

---

## Skills Demonstrated

- Log analysis
- Threat detection
- SIEM fundamentals
- Python scripting
- Database handling
- Web development
- Security monitoring

---

## Author

Yash Nandi
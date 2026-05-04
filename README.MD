# Mini SIEM - Security Log Monitoring & Threat Detection

A beginner-friendly Security Information and Event Management (SIEM) project built using Python, Flask, and SQLite.

This project parses security logs, detects suspicious activity, stores incidents in a database, and displays alerts in a dashboard.

---

## Dashboard Preview


### Logs View
[Logs Dashboard](Screenshots/Dashboard1.png)

### Alerts View
[Alerts Dashboard](Screenshots/Dashboard2.png)

---

## Features

### Brute Force Detection
Detects repeated failed login attempts from the same IP.

Rule:
- More than 3 failed login attempts from the same IP

Example:
FAILED_LOGIN admin 192.168.1.20

---

### Port Scan Detection
Detects when one IP accesses multiple unique ports.

Rule:
- 4 or more unique ports accessed by the same IP

Example:
PORT_ACCESS 192.168.1.50 22
PORT_ACCESS 192.168.1.50 80
PORT_ACCESS 192.168.1.50 443
PORT_ACCESS 192.168.1.50 3306

---

### Password Spraying Detection
Detects one IP attempting multiple usernames.

Rule:
- 4 or more different usernames targeted from one IP

Example:
FAILED_LOGIN admin 192.168.1.80
FAILED_LOGIN user1 192.168.1.80
FAILED_LOGIN user2 192.168.1.80
FAILED_LOGIN user3 192.168.1.80

---

## Tech Stack

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
│── .gitignore  
│── logs/  
│   └── sample.log  
│── templates/  
│   └── dashboard.html  
│── screenshots/  
│   └── dashboard.png  

---

## Installation

Clone the repository:

git clone <your-repository-url>

Move into project folder:

cd mini-siem

Install dependencies:

pip install -r requirements.txt

---

## Run Project

Start Flask server:

python app.py

Open in browser:

http://127.0.0.1:5000

---

## Supported Log Formats

Login events:

YYYY-MM-DD HH:MM:SS FAILED_LOGIN username ip

Example:

2026-05-03 09:01:15 FAILED_LOGIN admin 192.168.1.20

Port access events:

YYYY-MM-DD HH:MM:SS PORT_ACCESS ip port

Example:

2026-05-03 09:03:00 PORT_ACCESS 192.168.1.50 22

---

## Detection Logic

Brute Force Detection:
- Count failed login attempts per IP
- Alert when count > 3

Port Scan Detection:
- Count unique ports accessed per IP
- Alert when count >= 4

Password Spraying Detection:
- Count unique usernames targeted by same IP
- Alert when count >= 4

---

## Dashboard Features

Displays:
- Security logs
- Alert type
- Source IP
- Attack count
- Port information
- Username information

---

## Skills Demonstrated

- SIEM fundamentals
- Log analysis
- Threat detection
- Python scripting
- Flask web development
- Database management
- Security monitoring

---

## Future Improvements

- Real-time log monitoring
- Email alerts
- GeoIP tracking
- Threat intelligence integration
- Charts and analytics
- Export reports

---

## Author

Yash Nandi
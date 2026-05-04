import sqlite3

DB_NAME = "siem.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            username TEXT,
            ip_address TEXT,
            port TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_type TEXT,
            ip_address TEXT,
            count INTEGER
        )
    """)

    conn.commit()
    conn.close()


def clear_old_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM logs")
    cursor.execute("DELETE FROM alerts")

    conn.commit()
    conn.close()


def save_logs(logs):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for log in logs:
        cursor.execute("""
            INSERT INTO logs (
                timestamp,
                event_type,
                username,
                ip_address,
                port
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            log.get("timestamp"),
            log.get("event_type"),
            log.get("username"),
            log.get("ip_address"),
            log.get("port")
        ))

    conn.commit()
    conn.close()


def save_alerts(alerts):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for alert in alerts:
        cursor.execute("""
            INSERT INTO alerts (
                alert_type,
                ip_address,
                count
            )
            VALUES (?, ?, ?)
        """, (
            alert["alert_type"],
            alert["ip_address"],
            alert["count"]
        ))

    conn.commit()
    conn.close()


def get_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    conn.close()
    return logs


def get_alerts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()

    conn.close()
    return alerts
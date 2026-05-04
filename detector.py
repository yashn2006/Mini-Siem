def detect_brute_force(logs):
    failed_attempts = {}
    alerts = []

    for log in logs:
        if log["event_type"] == "FAILED_LOGIN":
            ip = log["ip_address"]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    for ip, count in failed_attempts.items():
        if count > 3:
            alerts.append({
                "alert_type": "Brute Force Attack",
                "ip_address": ip,
                "count": count
            })

    return alerts


def detect_port_scan(logs):
    port_access = {}
    alerts = []

    for log in logs:
        if log["event_type"] == "PORT_ACCESS":
            ip = log["ip_address"]
            port = log["port"]

            if ip not in port_access:
                port_access[ip] = set()

            port_access[ip].add(port)

    for ip, ports in port_access.items():
        if len(ports) >= 4:
            alerts.append({
                "alert_type": "Port Scanning Detected",
                "ip_address": ip,
                "count": len(ports)
            })

    return alerts


def detect_password_spraying(logs):
    spray_attempts = {}
    alerts = []

    for log in logs:
        if log["event_type"] == "FAILED_LOGIN":
            ip = log["ip_address"]
            username = log["username"]

            if ip not in spray_attempts:
                spray_attempts[ip] = set()

            spray_attempts[ip].add(username)

    for ip, users in spray_attempts.items():
        if len(users) >= 4:
            alerts.append({
                "alert_type": "Password Spraying Attack",
                "ip_address": ip,
                "count": len(users)
            })

    return alerts
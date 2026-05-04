from flask import Flask, render_template
from log_parser import parse_logs
from detector import (
    detect_brute_force,
    detect_port_scan,
    detect_password_spraying
)
from database import (
    init_db,
    clear_old_data,
    save_logs,
    save_alerts,
    get_logs,
    get_alerts
)

app = Flask(__name__)

LOG_FILE = "logs/sample.log"


@app.route("/")
def dashboard():
    logs = parse_logs(LOG_FILE)

    clear_old_data()
    save_logs(logs)

    alerts = []
    alerts.extend(detect_brute_force(logs))
    alerts.extend(detect_port_scan(logs))
    alerts.extend(detect_password_spraying(logs))

    save_alerts(alerts)

    all_logs = get_logs()
    all_alerts = get_alerts()

    return render_template(
        "dashboard.html",
        logs=all_logs,
        alerts=all_alerts
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
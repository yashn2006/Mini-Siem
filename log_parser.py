def parse_logs(filename):
    parsed_logs = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) >= 5:
                timestamp = parts[0] + " " + parts[1]
                event_type = parts[2]

                if event_type in ["FAILED_LOGIN", "SUCCESS_LOGIN"]:
                    username = parts[3]
                    ip_address = parts[4]

                    parsed_logs.append({
                        "timestamp": timestamp,
                        "event_type": event_type,
                        "username": username,
                        "ip_address": ip_address
                    })

                elif event_type == "PORT_ACCESS":
                    ip_address = parts[3]
                    port = parts[4]

                    parsed_logs.append({
                        "timestamp": timestamp,
                        "event_type": event_type,
                        "ip_address": ip_address,
                        "port": port
                    })

    return parsed_logs
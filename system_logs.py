import json
import shutil
import csv
import datetime

def load_logs():
    try:
        with open("logs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No logs records found.")
        return []
    except json.JSONDecodeError:
        print("Error: logs.json is empty or corrupted.")
        return []

def save_logs(logs):
    try: 
        with open("logs.json", "w") as file:
            json.dump(logs, file, indent=4)
        print("logs saved successfully.")
    except Exception as error:
        print(f"Error saving logs: {error}")

def backup_logs():
    try:
        shutil.copy("logs.json", "backup_logs.json")
        print("Backup Created Successfully.")
    except FileNotFoundError:
        print("logs.json file not found.")

def restore_logs():
    try:
        shutil.copy("backup_logs.json", "logs.json")
        print("Restore Successful.")
        return load_logs()
    except FileNotFoundError:
        print("Backup File Not Found.")
        return []

def log_login(logs, username, action):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = {
        "type": "Login",
        "user": username,
        "action": action,
        "timestamp": timestamp
    }

    logs.append(log)
    save_logs(logs)

def log_activity(logs, username, action):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = {
        "type": "Activity",
        "user": username,
        "action": action,
        "timestamp": timestamp
    }

    logs.append(log)

    save_logs(logs)

def log_error(logs, username, action):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = {
        "type": "Activity",
        "user": username,
        "action": action,
        "timestamp": timestamp
    }

    logs.append(log)

    save_logs(logs)

def view_login_logs(logs):

    login_logs = [log for log in logs if log["type"] == "Login"]

    if len(login_logs) == 0:
        print("No Login Logs Found.")
        return

    print("\n===== Login Logs =====")

    for count, log in enumerate(login_logs, start=1):
        print(f"\nLog {count}")
        print(f"User      : {log['user']}")
        print(f"Action    : {log['action']}")
        print(f"Timestamp : {log['timestamp']}")

def view_activity_logs(logs):

    if len(logs) == 0:
        print("No Activity Logs Found.")
        return

    print("\n===== Activity Logs =====")

    count = 1

    for log in logs:

        if log["type"] == "Activity":

            print(f"\nLog {count}")
            print(f"User      : {log['user']}")
            print(f"Action    : {log['action']}")
            print(f"Timestamp : {log['timestamp']}")

            count += 1

    if count == 1:
        print("No Activity Logs Found.")

def view_error_logs(logs):

    if len(logs) == 0:
        print("No Error Logs Found.")
        return

    print("\n===== Error Logs =====")

    count = 1

    for log in logs:

        if log["type"] == "Error":

            print(f"\nLog {count}")
            print(f"User      : {log['user']}")
            print(f"Action    : {log['action']}")
            print(f"Timestamp : {log['timestamp']}")

            count += 1

    if count == 1:
        print("No Error Logs Found.")

def export_logs_csv(logs):

    if len(logs) == 0:
        print("No log records found.")
        return

    try:
        with open("logs.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Type",
                "User",
                "Action",
                "Timestamp"
            ])

            for log in logs:

                writer.writerow([
                    log["type"],
                    log["user"],
                    log["action"],
                    log["timestamp"]
                ])

        print("Logs exported successfully.")

    except Exception as error:
        print(f"Error exporting logs: {error}")

def import_logs_csv():

    logs = []

    try:
        with open("logs.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                log = {
                    "type": row["Type"],
                    "user": row["User"],
                    "action": row["Action"],
                    "timestamp": row["Timestamp"]
                }

                logs.append(log)

        save_logs(logs)

        print("Logs imported successfully.")

        return logs

    except FileNotFoundError:
        print("logs.csv file not found.")
        return load_logs()

    except Exception as error:
        print(f"Error importing logs: {error}")
        return load_logs()

# Menu
def logging_menu():

    logs = load_logs()

    while True:

        print("\n===== Logging Module =====")
        print("1. View Login Logs")
        print("2. View Activity Logs")
        print("3. View Error Logs")
        print("4. Backup Logs")
        print("5. Restore Logs")
        print("6. CSV Export")
        print("7. CSV Import")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            view_login_logs(logs)

        elif choice == "2":
            view_activity_logs(logs)

        elif choice == "3":
            view_error_logs(logs)

        elif choice == "4":
            backup_logs()

        elif choice == "5":
            logs = restore_logs()

        elif choice == "6":
            export_logs_csv(logs)

        elif choice == "7":
            logs = import_logs_csv()

        elif choice == "8":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
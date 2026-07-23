from student import *
from attendance import *
from marks import *
from gpa import *
from subjects import *
from teachers import *
from users import *
from system_logs import *
import os #view
import sqlite3

#json database
def json_database_menu():

    while True:

        print("\n========== JSON Database ==========")
        print("1. Save All Data")
        print("2. Load All Data")
        print("3. View JSON Files")
        print("4. Delete JSON Files")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            save_all()

        elif choice == "2":
            load_all()

        elif choice == "3":
            view_json_files()

        elif choice == "4":
            delete_json_files()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")

def save_all():

    save_students(load_students())
    save_attendance(load_attendance())
    save_marks(load_marks())
    save_gpa(load_gpa())
    save_subjects(load_subjects())
    save_teachers(load_teachers())
    save_users(load_users())
    save_logs(load_logs())

    print("\nAll JSON data saved successfully.")

def load_all():

    students = load_students()
    attendance = load_attendance()
    marks = load_marks()
    gpa = load_gpa()
    subjects = load_subjects()
    teachers = load_teachers()
    users = load_users()
    logs = load_logs()

    print("\nAll JSON data loaded successfully.")

    return {
        "students": students,
        "attendance": attendance,
        "marks": marks,
        "gpa": gpa,
        "subjects": subjects,
        "teachers": teachers,
        "users": users,
        "logs": logs
    }

def view_json_files():

    files = [
        "students.json",
        "attendance.json",
        "marks.json",
        "gpa.json",
        "subjects.json",
        "teachers.json",
        "users.json",
        "logs.json"
    ]

    print("\n========== JSON Files ==========")

    for file in files:
        if os.path.exists(file):
            print(f"✔ {file}")
        else:
            print(f"✘ {file} (Not Found)")

def delete_json_files():

    files = [
        "students.json",
        "attendance.json",
        "marks.json",
        "gpa.json",
        "subjects.json",
        "teachers.json",
        "users.json",
        "logs.json"
    ]

    confirm = input("Delete ALL JSON files? (Y/N): ").upper()

    if confirm != "Y":
        print("Deletion cancelled.")
        return

    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} deleted.")
        else:
            print(f"{file} not found.")

    print("\nAll available JSON files deleted.")

#csv database
def csv_database_menu():

    while True:

        print("\n========== CSV Database ==========")
        print("1. Export All CSV")
        print("2. Import All CSV")
        print("3. View CSV Files")
        print("4. Delete CSV Files")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            export_all_csv()

        elif choice == "2":
            import_all_csv()

        elif choice == "3":
            view_csv_files()

        elif choice == "4":
            delete_csv_files()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")

def export_all_csv():

    export_csv(load_students())
    export_attendance_csv(load_attendance())
    export_marks_csv(load_marks())
    export_gpa_csv()
    export_subjects_csv(load_subjects())
    export_teachers_csv(load_teachers())
    export_users_csv(load_users())
    export_logs_csv(load_logs())

    print("\nAll CSV files exported successfully.")

def import_all_csv():

    import_csv()
    import_attendance_csv()
    import_marks_csv()
    import_gpa_csv()
    import_subjects_csv()
    import_teachers_csv()
    import_users_csv()
    import_logs_csv()

    print("\nAll CSV files imported successfully.")

def view_csv_files():

    files = [
        "students.csv",
        "attendance.csv",
        "marks.csv",
        "gpa.csv",
        "subjects.csv",
        "teachers.csv",
        "users.csv",
        "logs.csv"
    ]

    print("\n========== CSV Files ==========")

    for file in files:
        if os.path.exists(file):
            print(f"✔ {file}")
        else:
            print(f"✘ {file} (Not Found)")

def delete_csv_files():

    files = [
        "students.csv",
        "attendance.csv",
        "marks.csv",
        "gpa.csv",
        "subjects.csv",
        "teachers.csv",
        "users.csv",
        "logs.csv"
    ]

    confirm = input("Delete ALL CSV files? (Y/N): ").upper()

    if confirm != "Y":
        print("Deletion cancelled.")
        return

    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} deleted.")
        else:
            print(f"{file} not found.")

    print("\nAll available CSV files deleted.")

#backup database
def backup_database_menu():

    while True:

        print("\n========== Backup Database ==========")
        print("1. Backup All")
        print("2. View Backup Files")
        print("3. Delete Backup Files")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            backup_all()

        elif choice == "2":
            view_backup_files()

        elif choice == "3":
            delete_backup_files()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")

def backup_all():

    backup_students()
    backup_attendance()
    backup_marks()
    backup_gpa()
    backup_subjects()
    backup_teachers()
    backup_users()
    backup_logs()

    print("\nAll data backed up successfully.")

def view_backup_files():

    files = [
        "backup_students.json",
        "backup_attendance.json",
        "backup_marks.json",
        "backup_gpa.json",
        "backup_subjects.json",
        "backup_teachers.json",
        "backup_users.json",
        "backup_logs.json"
    ]

    print("\n========== Backup Files ==========")

    for file in files:
        if os.path.exists(file):
            print(f"✔ {file}")
        else:
            print(f"✘ {file} (Not Found)")

def delete_backup_files():

    files = [
        "backup_students.json",
        "backup_attendance.json",
        "backup_marks.json",
        "backup_gpa.json",
        "backup_subjects.json",
        "backup_teachers.json",
        "backup_users.json",
        "backup_logs.json"
    ]

    confirm = input("Delete ALL backup files? (Y/N): ").upper()

    if confirm != "Y":
        print("Deletion cancelled.")
        return

    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} deleted.")
        else:
            print(f"{file} not found.")

    print("\nAll available backup files deleted.")

#restore database
def restore_database_menu():

    while True:

        print("\n========== Restore Database ==========")
        print("1. Restore All")
        print("2. View Backup Files")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            restore_all()

        elif choice == "2":
            view_backup_files()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")

def restore_all():

    restore_students()
    restore_attendance()
    restore_marks()
    restore_gpa()
    restore_subjects()
    restore_teachers()
    restore_users()
    restore_logs()

    print("\nAll data restored successfully.")

def view_backup_files():

    files = [
        "backup_students.json",
        "backup_attendance.json",
        "backup_marks.json",
        "backup_gpa.json",
        "backup_subjects.json",
        "backup_teachers.json",
        "backup_users.json",
        "backup_logs.json"
    ]

    print("\n========== Backup Files ==========")

    for file in files:
        if os.path.exists(file):
            print(f"✔ {file}")
        else:
            print(f"✘ {file} (Not Found)")

#sqlie database
def sqlite_database_menu():

    while True:

        print("\n========== SQLite Database ==========")
        print("1. Create Database")
        print("2. Create Tables")
        print("3. Migrate JSON to SQLite")
        print("4. View Tables")
        print("5. Delete Database")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_database()

        elif choice == "2":
            create_tables()

        elif choice == "3":
            json_to_sqlite()

        elif choice == "4":
            view_tables()

        elif choice == "5":
            delete_database()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")

def create_database():

    conn = sqlite3.connect("sms.db")

    conn.close()

    print("\nSQLite database created successfully.")

def create_tables():

    conn = sqlite3.connect("sms.db")
    cursor = conn.cursor()

    # Students
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            rollno INTEGER PRIMARY KEY,
            name TEXT,
            grade TEXT
        )
    """)

    # Attendance
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rollno INTEGER,
            date TEXT,
            status TEXT
        )
    """)

    # Marks
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rollno INTEGER,
            subject TEXT,
            marks REAL
        )
    """)

    # GPA
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gpa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rollno INTEGER,
            total REAL,
            average REAL,
            gpa REAL,
            grade TEXT,
            date TEXT
        )
    """)

    # Subjects
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_code TEXT,
            subject_name TEXT,
            credits INTEGER
        )
    """)

    # Teachers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            teacher_id INTEGER PRIMARY KEY,
            name TEXT,
            gender TEXT,
            phone TEXT,
            email TEXT,
            subject TEXT,
            class TEXT,
            created_at TEXT
        )
    """)

    # Users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT,
            role TEXT,
            created_at TEXT
        )
    """)

    # Logs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            user TEXT,
            action TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("\nAll tables created successfully.")

def json_to_sqlite():

    students = load_students()
    attendance = load_attendance()
    marks = load_marks()
    gpa = load_gpa()
    subjects = load_subjects()
    teachers = load_teachers()
    users = load_users()
    logs = load_logs()

    conn = sqlite3.connect("sms.db")
    cursor = conn.cursor()

    # Students
    # Clear table once
    cursor.execute("DELETE FROM students")
    for student in students:
        cursor.execute("""
            INSERT OR REPLACE INTO students
            (rollno, name, grade)
            VALUES (?, ?, ?)
        """, (
            student["rollno"],
            student["name"],
            student["grade"]
        ))

    # Attendance
    # Clear table once
    cursor.execute("DELETE FROM attendance")

    for record in attendance:
        cursor.execute("""
            INSERT INTO attendance
            (rollno, date, status)
            VALUES (?, ?, ?)
        """, (
            record["rollno"],
            record["date"],
            record["status"]
        ))

    # Marks
    # Clear table once
    cursor.execute("DELETE FROM marks")
    for student in marks:

        rollno = student["rollno"]

        for subject, mark in student["subjects"].items():

            cursor.execute("""
                INSERT INTO marks
                (rollno, subject, marks)
                VALUES (?, ?, ?)
            """, (
                rollno,
                subject,
                mark
            ))

    # GPA
    # Clear table once
    cursor.execute("DELETE FROM gpa")
    for item in gpa:
        cursor.execute("""
            INSERT INTO gpa
            (rollno, total, average, gpa, grade, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item["rollno"],
            item["total"],
            item["average"],
            item["gpa"],
            item["grade"],
            item["date"]
        ))

    # Subjects
    # Clear table once
    cursor.execute("DELETE FROM subjects")
    for subject in subjects:
        cursor.execute("""
            INSERT INTO subjects
            (subject_code, subject_name, credits)
            VALUES (?, ?, ?)
        """, (
            subject["subject_code"],
            subject["subject_name"],
            subject["credits"]
        ))

    # Teachers
    # Clear table once
    cursor.execute("DELETE FROM teachers")
    for teacher in teachers:
        cursor.execute("""
            INSERT INTO teachers
            (teacher_id, name, gender, phone, email, subject, class, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            teacher["teacher_id"],
            teacher["name"],
            teacher["gender"],
            teacher["phone"],
            teacher["email"],
            teacher["subject"],
            teacher["class"],
            teacher["created_at"]
        ))

    # Users
    # Clear table once
    cursor.execute("DELETE FROM users")
    for user in users:
        cursor.execute("""
            INSERT INTO users
            (username, email, password, role, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            user["username"],
            user["email"],
            user["password"],
            user["role"],
            user["created_at"]
        ))

    # Logs
    # Clear table once
    cursor.execute("DELETE FROM logs")
    for log in logs:
        cursor.execute("""
            INSERT INTO logs
            (type, user, action, timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            log["type"],
            log["user"],
            log["action"],
            log["timestamp"]
        ))

    conn.commit()
    conn.close()

    print("\nJSON data migrated to SQLite successfully.")

def view_tables():

    conn = sqlite3.connect("sms.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = cursor.fetchall()

    if len(tables) == 0:
        print("\nNo tables found.")

    else:
        print("\n========== SQLite Tables ==========")

        for table in tables:
            print(table[0])

    conn.close()

def delete_database():

    if not os.path.exists("sms.db"):
        print("\nDatabase not found.")
        return

    confirm = input("Delete SQLite Database? (Y/N): ").upper()

    if confirm != "Y":
        print("Deletion cancelled.")
        return

    os.remove("sms.db")

    print("\nSQLite database deleted successfully.")

def database_menu():

    while True:

        print("\n========== Database Module ==========")
        print("1. JSON Database")
        print("2. CSV Database")
        print("3. Backup Database")
        print("4. Restore Database")
        print("5. SQLite Database")
        print("0. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            json_database_menu()

        elif choice == "2":
            csv_database_menu()

        elif choice == "3":
            backup_database_menu()

        elif choice == "4":
            restore_database_menu()

        elif choice == "5":
            sqlite_database_menu()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")
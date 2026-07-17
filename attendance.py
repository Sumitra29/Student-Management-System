import json
import shutil
import csv
import datetime
from student import *

# Attendance CRUD
def mark_attendance(attendance):

    students = load_students()

    if len(students) == 0:
        print("No Student Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    student_found = False

    for student in students:
        if student["rollno"] == rollno:
            student_found = True

            print("\nStudent Found")
            print("-" * 35)
            print(f"Name    : {student['name']}")
            print(f"Grade   : {student['grade']}")
            print(f"Roll No : {student['rollno']}")
            break

    if not student_found:
        print("Student not found.")
        return

    today = datetime.date.today().strftime("%Y-%m-%d")

    # Prevent duplicate attendance
    for record in attendance:
        if record["rollno"] == rollno and record["date"] == today:
            print("Attendance already marked for today.")
            return

    print("\nAttendance Status")
    print("1. Present")
    print("2. Absent")

    choice = input("Enter Choice: ")

    if choice == "1":
        status = "Present"

    elif choice == "2":
        status = "Absent"

    else:
        print("Invalid Choice.")
        return

    record = {
        "rollno": rollno,
        "date": today,
        "status": status
    }

    attendance.append(record)

    save_attendance(attendance)

    print("Attendance marked successfully.")

#def view_attendance(attendance):
    #pass
def view_attendance(attendance):

    if len(attendance) == 0:
        print("\nNo Attendance Record Found.\n")
        return

    print("\nAttendance Records")
    print("=" * 45)

    for index, record in enumerate(attendance, start=1):

        print(f"Record {index}")
        print("-" * 45)
        print(f"Roll No : {record['rollno']}")
        print(f"Date    : {record['date']}")
        print(f"Status  : {record['status']}")
        print()

#def search_attendance(attendance):
    #pass
def search_attendance(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    print("\nSearch Attendance")
    print("1. Search by Roll No")
    print("2. Search by Date")

    choice = input("Enter Choice: ")

    if choice == "1":

        try:
            rollno = int(input("Enter Roll No: "))
        except ValueError:
            print("Invalid Roll Number.")
            return

        found = False

        for record in attendance:

            if record["rollno"] == rollno:

                print("\nAttendance Found")
                print("-" * 35)
                print(f"Roll No : {record['rollno']}")
                print(f"Date    : {record['date']}")
                print(f"Status  : {record['status']}")
                found = True

        if not found:
            print("Attendance not found.")

    elif choice == "2":

        date = input("Enter Date (YYYY-MM-DD): ").strip()

        found = False

        for record in attendance:

            if record["date"] == date:

                print("\nAttendance Found")
                print("-" * 35)
                print(f"Roll No : {record['rollno']}")
                print(f"Date    : {record['date']}")
                print(f"Status  : {record['status']}")
                found = True

        if not found:
            print("Attendance not found.")

    else:
        print("Invalid Choice.")

#def update_attendance(attendance):
    #pass
def update_attendance(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    for record in attendance:

        if record["rollno"] == rollno and record["date"] == date:

            print("\nAttendance Found")
            print("-" * 35)
            print(f"Roll No : {record['rollno']}")
            print(f"Date    : {record['date']}")
            print(f"Status  : {record['status']}")

            print("\nUpdate Attendance")
            print("1. Present")
            print("2. Absent")

            choice = input("Enter Choice: ")

            if choice == "1":
                record["status"] = "Present"

            elif choice == "2":
                record["status"] = "Absent"

            else:
                print("Invalid Choice.")
                return

            save_attendance(attendance)

            print("Attendance updated successfully.")
            return

    print("Attendance record not found.")

#def delete_attendance(attendance):
    #pass
def delete_attendance(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    for record in attendance:

        if record["rollno"] == rollno and record["date"] == date:

            print("\nAttendance Found")
            print("-" * 35)
            print(f"Roll No : {record['rollno']}")
            print(f"Date    : {record['date']}")
            print(f"Status  : {record['status']}")

            choice = input("\nAre you sure you want to delete? (Y/N): ").strip().upper()

            if choice == "Y":

                attendance.remove(record)

                save_attendance(attendance)

                print("Attendance deleted successfully.")

            else:
                print("Deletion cancelled.")

            return

    print("Attendance record not found.")

# Attendance Features
#def attendance_history(attendance):
    #pass
def attendance_history(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    history = []

    for record in attendance:
        if record["rollno"] == rollno:
            history.append(record)

    if len(history) == 0:
        print("No Attendance History Found.")
        return

    history.sort(key=lambda record: record["date"])

    print("\nAttendance History")
    print("=" * 40)

    for index, record in enumerate(history, start=1):
        print(f"Record {index}")
        print("-" * 40)
        print(f"Roll No : {record['rollno']}")
        print(f"Date    : {record['date']}")
        print(f"Status  : {record['status']}")
        print()

#def attendance_percentage(attendance):
    #pass
def attendance_percentage(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    total_days = 0
    present_days = 0

    for record in attendance:

        if record["rollno"] == rollno:

            total_days += 1

            if record["status"] == "Present":
                present_days += 1

    if total_days == 0:
        print("No Attendance Record Found for this student.")
        return

    percentage = (present_days / total_days) * 100

    print("\nAttendance Summary")
    print("-" * 35)
    print(f"Roll No         : {rollno}")
    print(f"Total Days      : {total_days}")
    print(f"Present Days    : {present_days}")
    print(f"Absent Days     : {total_days - present_days}")
    print(f"Attendance      : {percentage:.2f}%")

#def present_students(attendance):
    #pass
def present_students(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    found = False

    print("\nPresent Students")
    print("=" * 40)

    for record in attendance:

        if record["date"] == date and record["status"] == "Present":

            print(f"Roll No : {record['rollno']}")
            print(f"Date    : {record['date']}")
            print(f"Status  : {record['status']}")
            print("-" * 40)

            found = True

    if not found:
        print("No Present Students Found.")

#def absent_students(attendance):
    #pass
def absent_students(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    found = False

    print("\nAbsent Students")
    print("=" * 40)

    for record in attendance:

        if record["date"] == date and record["status"] == "Absent":

            print(f"Roll No : {record['rollno']}")
            print(f"Date    : {record['date']}")
            print(f"Status  : {record['status']}")
            print("-" * 40)

            found = True

    if not found:
        print("No Absent Students Found.")

#def attendance_report(attendance):
    #pass
def attendance_report(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    total = 0
    present = 0
    absent = 0

    for record in attendance:

        if record["date"] == date:

            total += 1

            if record["status"] == "Present":
                present += 1

            elif record["status"] == "Absent":
                absent += 1

    if total == 0:
        print("No Attendance Record Found for this date.")
        return

    percentage = (present / total) * 100

    print("\nAttendance Report")
    print("=" * 40)
    print(f"Date                 : {date}")
    print(f"Total Students       : {total}")
    print(f"Present Students     : {present}")
    print(f"Absent Students      : {absent}")
    print(f"Attendance Percentage: {percentage:.2f}%")

# JSON
#def save_attendance(attendance):
    #pass
def save_attendance(attendance):

    try:
        with open("attendance.json", "w") as file:
            json.dump(attendance, file, indent=4)

        print("Attendance saved successfully.")

    except Exception as error:
        print(f"Error saving attendance: {error}")

#def load_attendance():
    #pass
def load_attendance():

    try:
        with open("attendance.json", "r") as file:
            attendance = json.load(file)

        print("Attendance loaded successfully.")
        return attendance

    except FileNotFoundError:
        print("No attendance records found.")
        return []

    except json.JSONDecodeError:
        print("Error: attendance.json is empty or corrupted.")
        return []

    except Exception as error:
        print(f"Error loading attendance: {error}")
        return []

# Backup
#def backup_attendance():
    #pass
def backup_attendance():

    try:
        shutil.copy("attendance.json", "backup_attendance.json")
        print("Attendance backup created successfully.")

    except FileNotFoundError:
        print("attendance.json not found.")

    except Exception as error:
        print(f"Error creating backup: {error}")

#def restore_attendance():
    #pass
def restore_attendance():

    try:
        shutil.copy("backup_attendance.json", "attendance.json")

        print("Attendance restored successfully.")

        return load_attendance()

    except FileNotFoundError:
        print("Backup file not found.")
        return []

    except Exception as error:
        print(f"Error restoring backup: {error}")
        return []

# CSV
#def export_attendance_csv(attendance):
    #pass
def export_attendance_csv(attendance):

    if len(attendance) == 0:
        print("No Attendance Record Found.")
        return

    try:

        with open("attendance.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Roll No", "Date", "Status"])

            for record in attendance:

                writer.writerow([
                    record["rollno"],
                    record["date"],
                    record["status"]
                ])

        print("Attendance exported successfully.")

    except Exception as error:
        print(f"Error exporting CSV: {error}")

#def import_attendance_csv():
    #pass
def import_attendance_csv():

    attendance = []

    try:

        with open("attendance.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                attendance.append({
                    "rollno": int(row["Roll No"]),
                    "date": row["Date"],
                    "status": row["Status"]
                })

        save_attendance(attendance)

        print("Attendance imported successfully.")

        return attendance

    except FileNotFoundError:
        print("attendance.csv not found.")
        return []

    except Exception as error:
        print(f"Error importing CSV: {error}")
        return []
        
# Menu
def attendance_menu():

    attendance = load_attendance()

    while True:

        print("\n===== Attendance Module =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Search Attendance")
        print("4. Update Attendance")
        print("5. Delete Attendance")
        print("6. Attendance History")
        print("7. Attendance Percentage")
        print("8. Present Students")
        print("9. Absent Students")
        print("10. Attendance Report")
        print("11. Save Attendance")
        print("12. Backup Attendance")
        print("13. Restore Attendance")
        print("14. CSV Export")
        print("15. CSV Import")
        print("16. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            mark_attendance(attendance)

        elif choice == "2":
            view_attendance(attendance)

        elif choice == "3":
            search_attendance(attendance)

        elif choice == "4":
            update_attendance(attendance)

        elif choice == "5":
            delete_attendance(attendance)

        elif choice == "6":
            attendance_history(attendance)

        elif choice == "7":
            attendance_percentage(attendance)

        elif choice == "8":
            present_students(attendance)

        elif choice == "9":
            absent_students(attendance)

        elif choice == "10":
            attendance_report(attendance)

        elif choice == "11":
            save_attendance(attendance)

        elif choice == "12":
            backup_attendance()

        elif choice == "13":
            attendance = restore_attendance()

        elif choice == "14":
            export_attendance_csv(attendance)

        elif choice == "15":
            attendance = import_attendance_csv()

        elif choice == "16":
            break

        else:
            print("Invalid Choice")
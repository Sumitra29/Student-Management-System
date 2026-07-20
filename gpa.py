import json
import shutil
import csv
import datetime
from marks import load_marks

#def calculate_gpa(gpa, marks):
    #pass
def calculate_gpa(gpa, marks):

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    for student in marks:

        if student["rollno"] == rollno:

            subject_count = len(student["subjects"])

            if subject_count == 0:
                print("No subjects found.")
                return

            total = sum(student["subjects"].values())
            average = total / subject_count
            gpa_value = round(average / 10, 2)

            grade = calculate_grade(average)

            record = {
                "rollno": rollno,
                "total": total,
                "average": average,
                "gpa": gpa_value,
                "grade": grade,
                "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }

            # Save every GPA calculation
            gpa.append(record)

            # Save to JSON
            save_gpa(gpa)

            print("GPA Calculated Successfully.")
            return

    print("Marks Record Not Found.")
    
#def view_gpa(gpa):
    #pass
def view_gpa(gpa):

    if len(gpa) == 0:
        print("No GPA records found.")
        return

    count = 1

    for student in gpa:

        print(f"\nGPA Record {count}")
        print("-" * 35)
        print(f"Roll No : {student['rollno']}")
        print(f"Total   : {student['total']}")
        print(f"Average : {student['average']:.2f}")
        print(f"GPA     : {student['gpa']:.2f}")
        print(f"Grade   : {student['grade']}")
        print(f"Date    : {student['date']}")

        count += 1

#def gpa_history(gpa):
    #pass
def gpa_history(gpa):

    if len(gpa) == 0:
        print("No GPA history found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    found = False
    count = 1

    print("\n===== GPA HISTORY =====")

    for record in gpa:

        if record["rollno"] == rollno:

            print(f"\nHistory {count}")
            print("-" * 35)
            print(f"Roll No : {record['rollno']}")
            print(f"Total   : {record['total']}")
            print(f"Average : {record['average']:.2f}")
            print(f"GPA     : {record['gpa']:.2f}")
            print(f"Grade   : {record['grade']}")
            print(f"Date    : {record['date']}")

            count += 1
            found = True

    if not found:
        print("No GPA history found for this student.")

#def calculate_grade(average):
    #pass
def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    return "F"

#def save_gpa(gpa):
    #pass
def save_gpa(gpa):
    try:
        with open("gpa.json", "w") as file:
            json.dump(gpa, file, indent=4)
        print("GPA data saved successfully.")

    except Exception as e:
        print("Error saving GPA:", e)

#def load_gpa():
    #pass
def load_gpa():
    try:
        with open("gpa.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

#def backup_gpa():
    #pass
def backup_gpa():

    try:
        shutil.copy("gpa.json", "backup_gpa.json")
        print("GPA backup created successfully.")

    except FileNotFoundError:
        print("No GPA file found to backup.")

    except Exception as e:
        print("Error:", e)

#def restore_gpa():
    #pass
def restore_gpa():

    try:
        shutil.copy("backup_gpa.json", "gpa.json")
        print("GPA restored successfully.")
        return load_gpa()

    except FileNotFoundError:
        print("No backup file found.")
        return []

    except Exception as e:
        print("Error:", e)
        return []

#def export_gpa_csv():
    #pass
def export_gpa_csv():

    gpa = load_gpa()

    if len(gpa) == 0:
        print("No GPA records found.")
        return

    with open("gpa.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Header
        writer.writerow(["Roll No", "Total", "Average", "GPA", "Grade", "Date"])

        # Data
        for student in gpa:
            writer.writerow([
                student["rollno"],
                student["total"],
                student["average"],
                student["gpa"],
                student["grade"],
                student["date"]
            ])

    print("GPA exported successfully.")

#def import_gpa_csv():
    #pass
def import_gpa_csv():

    gpa = []

    try:
        with open("gpa.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                record = {
                    "rollno": int(row["Roll No"]),
                    "total": int(row["Total"]),
                    "average": float(row["Average"]),
                    "gpa": float(row["GPA"]),
                    "grade": row["Grade"],
                    "date": row["Date"]
                }

                gpa.append(record)

        save_gpa(gpa)
        print("GPA imported successfully.")
        return gpa

    except FileNotFoundError:
        print("CSV file not found.")
        return []

    except Exception as e:
        print("Error:", e)
        return []

# Menu
def gpa_menu():

    marks = load_marks()
    gpa = load_gpa()

    while True:

        print("\n===== GPA Module =====")
        print("1. Calculate GPA")
        print("2. View GPA")
        print("3. GPA History")
        print("4. Calculate Grade")
        print("5. Save GPA")
        print("6. Backup GPA")
        print("7. Restore GPA")
        print("8. CSV Export")
        print("9. CSV Import")
        print("10. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            calculate_gpa(gpa, marks)

        elif choice == "2":
            view_gpa(gpa)

        elif choice == "3":
            gpa_history(gpa)

        elif choice == "4":
            try:
                average = float(input("Enter Average Marks: "))
                grade = calculate_grade(average)
                print(f"Grade: {grade}")
            except ValueError:
                print("Invalid Average.")

        elif choice == "5":
            save_gpa(gpa)

        elif choice == "6":
            backup_gpa()

        elif choice == "7":
            gpa = restore_gpa()

        elif choice == "8":
            export_gpa_csv()

        elif choice == "9":
            gpa = import_gpa_csv()

        elif choice == "10":
            break

        else:
            print("Invalid Choice")
import json
import shutil
import csv
import datetime
from student import load_students

#def add_marks(students, marks): #1
    #pass
def add_marks(students, marks):

    if len(students) == 0:
        print("No Student Records Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    # Check whether student exists
    student_found = False

    for student in students:
        if student["rollno"] == rollno:
            student_found = True
            break

    if not student_found:
        print("Student Not Found.")
        return

    # Check whether marks already exist
    for record in marks:
        if record["rollno"] == rollno:
            print("Marks Already Added.")
            return

    try:
        python = float(input("Enter Python Marks: "))
        math = float(input("Enter Math Marks: "))
        english = float(input("Enter English Marks: "))
    except ValueError:
        print("Marks must be numbers.")
        return

    record = {
        "rollno": rollno,
        "subjects": {
            "Python": python,
            "Math": math,
            "English": english
        }
    }

    marks.append(record)

    save_marks(marks)

    print("Marks Added Successfully.")

#def view_marks(marks): #2
    #pass
def view_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    count = 1

    for record in marks:
        print(f"\nStudent {count}")
        print("-" * 35)
        print(f"Roll No : {record['rollno']}")

        print("Subjects:")
        for subject, mark in record["subjects"].items():
            print(f"{subject:<10}: {mark}")

        count += 1

#def search_marks(marks): #3
    #pass
def search_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    for record in marks:

        if record["rollno"] == rollno:

            print("\nMarks Record Found")
            print("-" * 35)
            print(f"Roll No : {record['rollno']}")

            print("Subjects:")
            for subject, mark in record["subjects"].items():
                print(f"{subject:<10}: {mark}")

            return

    print("Marks Record Not Found.")

#def update_marks(marks): #4
    #pass
def update_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    for record in marks:

        if record["rollno"] == rollno:

            print("\nCurrent Marks")
            print("-" * 35)

            for subject, mark in record["subjects"].items():
                print(f"{subject:<10}: {mark}")

            subject = input("\nEnter Subject Name: ").strip().title()

            if subject not in record["subjects"]:
                print("Subject Not Found.")
                return

            try:
                new_marks = float(input("Enter New Marks: "))
            except ValueError:
                print("Invalid Marks.")
                return

            record["subjects"][subject] = new_marks

            save_marks(marks)

            print("Marks Updated Successfully.")
            return

    print("Marks Record Not Found.")

#def delete_marks(marks): #5
    #pass
def delete_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    for record in marks:

        if record["rollno"] == rollno:

            print("\nMarks Record Found")
            print("-" * 35)
            print(f"Roll No : {record['rollno']}")

            print("Subjects:")
            for subject, mark in record["subjects"].items():
                print(f"{subject:<10}: {mark}")

            confirm = input("\nAre you sure you want to delete? (Y/N): ").strip().upper()

            if confirm == "Y":
                marks.remove(record)
                save_marks(marks)
                print("Marks Deleted Successfully.")
            else:
                print("Deletion Cancelled.")

            return

    print("Marks Record Not Found.")

#def subject_wise_marks(marks): #6
    #pass
def subject_wise_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    subject = input("Enter Subject Name: ").strip().title()

    found = False

    print(f"\n{subject} Marks")
    print("-" * 35)

    for record in marks:

        if subject in record["subjects"]:
            print(f"Roll No : {record['rollno']}")
            print(f"{subject} : {record['subjects'][subject]}")
            print("-" * 35)
            found = True

    if not found:
        print("Subject Not Found.")

#def total_marks(marks): #7
    #pass
def total_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    for record in marks:

        if record["rollno"] == rollno:

            total = sum(record["subjects"].values())

            print("\nMarks")
            print("-" * 35)

            for subject, mark in record["subjects"].items():
                print(f"{subject:<10}: {mark}")

            print("-" * 35)
            print(f"Total Marks : {total}")

            return

    print("Marks Record Not Found.")

#def average_marks(marks): #8
    #pass
def average_marks(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid Roll No.")
        return

    for record in marks:

        if record["rollno"] == rollno:

            total = sum(record["subjects"].values())
            average = total / len(record["subjects"])

            print("\nMarks")
            print("-" * 35)

            for subject, mark in record["subjects"].items():
                print(f"{subject:<10}: {mark}")

            print("-" * 35)
            print(f"Total Marks   : {total}")
            print(f"Average Marks : {average:.2f}")

            return

    print("Marks Record Not Found.")

#def rank_students(marks): #9
    #pass
def rank_students(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    ranked = sorted(
        marks,
        key=lambda record: sum(record["subjects"].values()),
        reverse=True
    )

    print("\nStudent Rankings")
    print("-" * 50)
    print(f"{'Rank':<6}{'Roll No':<10}{'Total Marks'}")
    print("-" * 50)

    rank = 1

    for record in ranked:

        total = sum(record["subjects"].values())

        print(f"{rank:<6}{record['rollno']:<10}{total}")

        rank += 1

#JSON
#def save_marks(marks): #10
    #pass
def save_marks(marks):
    try: 
        with open("marks.json", "w") as file:
            json.dump(marks, file, indent=4)

        print("Marks saved successfully.")
    
    except Exception as error:
        print(f"Error saving marks: {error}")

#def load_marks(): 
    #pass
def load_marks():
    try:
        with open("marks.json", "r") as file:
            marks = json.load(file)

        print("Marks loaded successfully.")
        return marks

    except FileNotFoundError:
        print("No attendance records found.")
        return []

    except json.JSONDecodeError:
        print("Error: attendance.json is empty or corrupted.")
        return []
        
# Bcakup
#def backup_marks(): #11
    #pass
def backup_marks():

    try:
        shutil.copy("marks.json", "backup_marks.json")
        print("Backup Created Successfully.")
    except FileNotFoundError:
        print("marks.json file not found.")

#def restore_marks(): #12
    #pass
def restore_marks():

    try:
        shutil.copy("backup_marks.json", "marks.json")
        print("Restore Successful.")
        return load_marks()

    except FileNotFoundError:
        print("Backup File Not Found.")
        return []

#CSV
#def export_marks_csv(): #13
    #pass
def export_marks_csv(marks):

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    with open("marks.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Header
        writer.writerow(["Roll No", "Python", "Math", "English"])

        # Data
        for record in marks:

            writer.writerow([
                record["rollno"],
                record["subjects"]["Python"],
                record["subjects"]["Math"],
                record["subjects"]["English"]
            ])

    print("Marks Exported Successfully.")

#def import_marks_csv(): #14
    #pass
def import_marks_csv():

    marks = []

    try:
        with open("marks.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                record = {
                    "rollno": int(row["Roll No"]),
                    "subjects": {
                        "Python": float(row["Python"]),
                        "Math": float(row["Math"]),
                        "English": float(row["English"])
                    }
                }

                marks.append(record)

        save_marks(marks)

        print("Marks Imported Successfully.")

        return marks

    except FileNotFoundError:
        print("marks.csv File Not Found.")
        return []
               
# Menu
def marks_menu():

    marks = load_marks()
    students = load_students()

    while True:

        print("\n===== Marks Module =====")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Search Marks")
        print("4. Update Marks")
        print("5. Delete Marks")
        print("6. Subject-wise Marks")
        print("7. Total Marks")
        print("8. Average Marks")
        print("9. Rank Students")
        print("10. Save Marks")
        print("11. Backup Marks")
        print("12. Restore Marks")
        print("13. CSV Export")
        print("14. CSV Import")
        print("15. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_marks(students, marks)

        elif choice == "2":
            view_marks(marks)

        elif choice == "3":
            search_marks(marks)

        elif choice == "4":
            update_marks(marks)

        elif choice == "5":
            delete_marks(marks)

        elif choice == "6":
            subject_wise_marks(marks)

        elif choice == "7":
            total_marks(marks)

        elif choice == "8":
            average_marks(marks)

        elif choice == "9":
            rank_students(marks)

        elif choice == "10":
            save_marks(marks)

        elif choice == "11":
            backup_marks()

        elif choice == "12":
            marks = restore_marks()

        elif choice == "13":
            export_marks_csv(marks)

        elif choice == "14":
            marks = import_marks_csv()

        elif choice == "15":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
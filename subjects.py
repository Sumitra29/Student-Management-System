import json
import shutil
import csv
import datetime
from student import load_students, save_students

#def add_subject(subjects):
    #pass
def add_subject(subjects):

    subject_code = input("Enter Subject Code: ").strip().upper()

    if subject_code == "":
        print("Subject Code cannot be empty.")
        return

    # Duplicate Subject Code Check
    for subject in subjects:
        if subject["subject_code"] == subject_code:
            print("Subject Code already exists.")
            return

    subject_name = input("Enter Subject Name: ").strip()

    if subject_name == "":
        print("Subject Name cannot be empty.")
        return

    try:
        credits = int(input("Enter Subject Credits: "))

        if credits <= 0:
            print("Credits must be greater than 0.")
            return

    except ValueError:
        print("Credits must be an integer.")
        return

    subject = {
        "subject_code": subject_code,
        "subject_name": subject_name,
        "credits": credits
    }

    subjects.append(subject)
    save_subjects(subjects)

    print("Subject added successfully.")

#def view_subjects(subjects):
    #pass
def view_subjects(subjects):

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    count = 1

    for subject in subjects:
        print(f"\nSubject {count}")
        print("-" * 35)
        print(f"Subject Code : {subject['subject_code']}")
        print(f"Subject Name : {subject['subject_name']}")
        print(f"Credits      : {subject['credits']}")
        count += 1

#def search_subject(subjects):
    #pass
def search_subject(subjects):

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    print("\nSearch By")
    print("1. Subject Code")
    print("2. Subject Name")

    choice = input("Enter Choice: ")

    found = False

    if choice == "1":

        subject_code = input("Enter Subject Code: ").strip().upper()

        for subject in subjects:
            if subject["subject_code"] == subject_code:
                print("\nSubject Found")
                print("-" * 35)
                print(f"Subject Code : {subject['subject_code']}")
                print(f"Subject Name : {subject['subject_name']}")
                print(f"Credits      : {subject['credits']}")
                found = True
                break

    elif choice == "2":

        subject_name = input("Enter Subject Name: ").strip().lower()

        for subject in subjects:
            if subject["subject_name"].lower() == subject_name:
                print("\nSubject Found")
                print("-" * 35)
                print(f"Subject Code : {subject['subject_code']}")
                print(f"Subject Name : {subject['subject_name']}")
                print(f"Credits      : {subject['credits']}")
                found = True
                break

    else:
        print("Invalid Choice.")
        return

    if not found:
        print("Subject Not Found.")

#def update_subject(subjects):
    #pass
def update_subject(subjects):

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    subject_code = input("Enter Subject Code to Update: ").strip().upper()

    for subject in subjects:

        if subject["subject_code"] == subject_code:

            print("\nCurrent Subject Details")
            print("-" * 35)
            print(f"Subject Code : {subject['subject_code']}")
            print(f"Subject Name : {subject['subject_name']}")
            print(f"Credits      : {subject['credits']}")

            new_subject_code = input("Enter New Subject Code: ").strip().upper()

            if new_subject_code == "":
                print("Subject Code cannot be empty.")
                return

            # Duplicate Subject Code Check
            for s in subjects:
                if s["subject_code"] == new_subject_code and s != subject:
                    print("Subject Code already exists.")
                    return

            new_subject_name = input("Enter New Subject Name: ").strip()

            if new_subject_name == "":
                print("Subject Name cannot be empty.")
                return

            try:
                new_credits = int(input("Enter New Credits: "))

                if new_credits <= 0:
                    print("Credits must be greater than 0.")
                    return

            except ValueError:
                print("Credits must be an integer.")
                return

            subject["subject_code"] = new_subject_code
            subject["subject_name"] = new_subject_name
            subject["credits"] = new_credits

            save_subjects(subjects)

            print("Subject Updated Successfully.")
            return

    print("Subject Not Found.")

#def delete_subject(subjects):
    #pass
def delete_subject(subjects):

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    subject_code = input("Enter Subject Code to Delete: ").strip().upper()

    for subject in subjects:

        if subject["subject_code"] == subject_code:

            print("\nSubject Found")
            print("-" * 35)
            print(f"Subject Code : {subject['subject_code']}")
            print(f"Subject Name : {subject['subject_name']}")
            print(f"Credits      : {subject['credits']}")

            confirm = input("\nAre you sure you want to delete? (Y/N): ").strip().upper()

            if confirm == "Y":
                subjects.remove(subject)
                save_subjects(subjects)
                print("Subject Deleted Successfully.")
            else:
                print("Delete Cancelled.")

            return

    print("Subject Not Found.")

#def assign_subject(students, subjects):
    #pass
def assign_subject(students, subjects):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    try:
        rollno = int(input("Enter Student Roll No: "))
    except ValueError:
        print("Roll No must be an integer.")
        return

    student = None

    for s in students:
        if s["rollno"] == rollno:
            student = s
            break

    if student is None:
        print("Student Not Found.")
        return

    subject_code = input("Enter Subject Code: ").strip().upper()

    subject = None

    for sub in subjects:
        if sub["subject_code"] == subject_code:
            subject = sub
            break

    if subject is None:
        print("Subject Not Found.")
        return

    # Create subjects list if it doesn't exist
    if "subjects" not in student:
        student["subjects"] = []

    # Prevent duplicate assignment
    if subject_code in student["subjects"]:
        print("Subject already assigned to this student.")
        return

    student["subjects"].append(subject_code)

    save_students(students)

    print("Subject Assigned Successfully.")

#def view_student_subjects(students, subjects):
    #pass
def view_student_subjects(students, subjects):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    try:
        rollno = int(input("Enter Student Roll No: "))
    except ValueError:
        print("Roll No must be an integer.")
        return

    for student in students:

        if student["rollno"] == rollno:

            print("\nStudent Details")
            print("-" * 35)
            print(f"Name     : {student['name']}")
            print(f"Grade    : {student['grade']}")
            print(f"Roll No  : {student['rollno']}")

            if "subjects" not in student or len(student["subjects"]) == 0:
                print("\nNo Subjects Assigned.")
                return

            print("\nAssigned Subjects")
            print("-" * 35)

            count = 1

            for subject_code in student["subjects"]:

                for subject in subjects:

                    if subject["subject_code"] == subject_code:

                        print(f"Subject {count}")
                        print(f"Code    : {subject['subject_code']}")
                        print(f"Name    : {subject['subject_name']}")
                        print(f"Credits : {subject['credits']}")
                        print("-" * 35)

                        count += 1

            return

    print("Student Not Found.")

#def remove_subject(students, subjects):
    #pass
def remove_subject(students, subjects):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    try:
        rollno = int(input("Enter Student Roll No: "))
    except ValueError:
        print("Roll No must be an integer.")
        return

    for student in students:

        if student["rollno"] == rollno:

            if "subjects" not in student or len(student["subjects"]) == 0:
                print("No Subjects Assigned.")
                return

            print("\nAssigned Subjects")
            print("-" * 35)

            for subject_code in student["subjects"]:

                for subject in subjects:

                    if subject["subject_code"] == subject_code:
                        print(f"{subject['subject_code']} - {subject['subject_name']}")

            remove_code = input("\nEnter Subject Code to Remove: ").strip().upper()

            if remove_code not in student["subjects"]:
                print("Subject is not assigned to this student.")
                return

            student["subjects"].remove(remove_code)

            save_students(students)

            print("Subject Removed Successfully.")
            return

    print("Student Not Found.")    

#def subject_credits(subjects):
    #pass
def subject_credits(subjects):

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    print("\n===== Subject Credits =====")

    for count, subject in enumerate(subjects, start=1):
        print(f"\nSubject {count}")
        print("-" * 35)
        print(f"Subject Code : {subject['subject_code']}")
        print(f"Subject Name : {subject['subject_name']}")
        print(f"Credits      : {subject['credits']}")

#def load_subjects():
    #pass
def load_subjects():
    try:
        with open("subjects.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No subjects records found.")
        return []
    except json.JSONDecodeError:
        print("Error: subjects.json is empty or corrupted.")
        return []

#def save_subjects(subjects):
    #pass
def save_subjects(subjects):
    try: 
        with open("subjects.json", "w") as file:
            json.dump(subjects, file, indent=4)
        print("Subjects saved successfully.")
    except Exception as error:
        print(f"Error saving Subjects: {error}")

#def backup_subjects():
    #pass
def backup_subjects():
    try:
        shutil.copy("subjects.json", "backup_subjects.json")
        print("Backup Created Successfully.")
    except FileNotFoundError:
        print("subjects.json file not found.")

#def restore_subjects():
    #pass
def restore_subjects():
    try:
        shutil.copy("backup_subjects.json", "subjects.json")
        print("Restore Successful.")
        return load_subjects()
    except FileNotFoundError:
        print("Backup File Not Found.")
        return []

#def export_subjects_csv(subjects):
    #pass
def export_subjects_csv(subjects):

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    try:
        with open("subjects.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Header
            writer.writerow(["Subject Code", "Subject Name", "Credits"])

            # Data
            for subject in subjects:
                writer.writerow([
                    subject["subject_code"],
                    subject["subject_name"],
                    subject["credits"]
                ])

        print("Subjects Exported Successfully.")

    except Exception as error:
        print(f"Error Exporting Subjects: {error}")

#def import_subjects_csv():
    #pass
def import_subjects_csv():

    subjects = []

    try:
        with open("subjects.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                subject = {
                    "subject_code": row["Subject Code"],
                    "subject_name": row["Subject Name"],
                    "credits": int(row["Credits"])
                }

                subjects.append(subject)

        save_subjects(subjects)

        print("Subjects Imported Successfully.")
        return subjects

    except FileNotFoundError:
        print("subjects.csv file not found.")
        return load_subjects()

    except Exception as error:
        print(f"Error Importing Subjects: {error}")
        return load_subjects()
        
# Menu
def subject_menu():

    students = load_students()
    subjects = load_subjects()

    while True:

        print("\n===== Subject Module =====")
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Search Subject")
        print("4. Update Subject")
        print("5. Delete Subject")
        print("6. Assign Subject")
        print("7. View Student Subjects")
        print("8. Remove Subject")
        print("9. Subject Credits")
        print("10. Save Subjects")
        print("11. Backup Subjects")
        print("12. Restore Subjects")
        print("13. CSV Export")
        print("14. CSV Import")
        print("15. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_subject(subjects)

        elif choice == "2":
            view_subjects(subjects)

        elif choice == "3":
            search_subject(subjects)

        elif choice == "4":
            update_subject(subjects)

        elif choice == "5":
            delete_subject(subjects)

        elif choice == "6":
            assign_subject(students, subjects)

        elif choice == "7":
            view_student_subjects(students, subjects)

        elif choice == "8":
            remove_subject(students, subjects)

        elif choice == "9":
            subject_credits(subjects)

        elif choice == "10":
            save_subjects(subjects)

        elif choice == "11":
            backup_subjects()

        elif choice == "12":
            subjects = restore_subjects()

        elif choice == "13":
            export_subjects_csv(subjects)

        elif choice == "14":
            subjects = import_subjects_csv()

        elif choice == "15":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
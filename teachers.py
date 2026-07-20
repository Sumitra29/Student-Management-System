import json
import shutil
import csv
import datetime
from student import load_students, save_students
from subjects import load_subjects

def load_teachers():
    try:
        with open("teachers.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No teachers records found.")
        return []
    except json.JSONDecodeError:
        print("Error: teachers.json is empty or corrupted.")
        return []

def save_teachers(teachers):
    try: 
        with open("teachers.json", "w") as file:
            json.dump(teachers, file, indent=4)
        print("teachers saved successfully.")
    except Exception as error:
        print(f"Error saving teachers: {error}")

def backup_teachers():
    try:
        shutil.copy("teachers.json", "backup_teachers.json")
        print("Backup Created Successfully.")
    except FileNotFoundError:
        print("teachers.json file not found.")

def restore_teachers():
    try:
        shutil.copy("backup_teachers.json", "teachers.json")
        print("Restore Successful.")
        return load_teachers()
    except FileNotFoundError:
        print("Backup File Not Found.")
        return []

#def add_teacher(teachers):
    #pass
def add_teacher(teachers):

    name = input("Enter Teacher Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    gender = input("Enter Gender: ").strip()

    if gender == "":
        print("Gender cannot be empty.")
        return

    phone = input("Enter Phone Number: ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("Phone number must contain exactly 10 digits.")
        return

    email = input("Enter Email: ").strip()

    if email == "":
        print("Email cannot be empty.")
        return

    try:
        teacher_id = int(input("Enter Teacher ID: "))
    except ValueError:
        print("Teacher ID must be an integer.")
        return

    # Duplicate Teacher ID
    for teacher in teachers:
        if teacher["teacher_id"] == teacher_id:
            print("Teacher ID already exists.")
            return

    # Duplicate Email
    for teacher in teachers:
        if teacher["email"].lower() == email.lower():
            print("Email already exists.")
            return

    teacher = {
        "teacher_id": teacher_id,
        "name": name,
        "gender": gender,
        "phone": phone,
        "email": email,
        "subject": "",
        "class": "",
        "created_at": str(datetime.date.today())
    }

    teachers.append(teacher)
    save_teachers(teachers)

    print("Teacher added successfully.")

#def view_teachers(teachers):
    #pass
def view_teachers(teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    count = 1

    for teacher in teachers:

        print(f"\nTeacher {count}")
        print("-" * 40)
        print(f"Teacher ID : {teacher['teacher_id']}")
        print(f"Name       : {teacher['name']}")
        print(f"Gender     : {teacher['gender']}")
        print(f"Phone      : {teacher['phone']}")
        print(f"Email      : {teacher['email']}")
        print(f"Subject    : {teacher['subject']}")
        print(f"Class      : {teacher['class']}")
        print(f"Created At : {teacher['created_at']}")

        count += 1    

#def search_teacher(teachers):
    #pass
def search_teacher(teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    print("\nSearch Teacher")
    print("1. Teacher ID")
    print("2. Teacher Name")

    choice = input("Enter Choice: ")

    found = False

    if choice == "1":

        try:
            teacher_id = int(input("Enter Teacher ID: "))
        except ValueError:
            print("Teacher ID must be an integer.")
            return

        for teacher in teachers:
            if teacher["teacher_id"] == teacher_id:

                print("\nTeacher Found")
                print("-" * 40)
                print(f"Teacher ID : {teacher['teacher_id']}")
                print(f"Name       : {teacher['name']}")
                print(f"Gender     : {teacher['gender']}")
                print(f"Phone      : {teacher['phone']}")
                print(f"Email      : {teacher['email']}")
                print(f"Subject    : {teacher['subject']}")
                print(f"Class      : {teacher['class']}")
                print(f"Created At : {teacher['created_at']}")

                found = True
                break

    elif choice == "2":

        name = input("Enter Teacher Name: ").strip().lower()

        for teacher in teachers:
            if teacher["name"].lower() == name:

                print("\nTeacher Found")
                print("-" * 40)
                print(f"Teacher ID : {teacher['teacher_id']}")
                print(f"Name       : {teacher['name']}")
                print(f"Gender     : {teacher['gender']}")
                print(f"Phone      : {teacher['phone']}")
                print(f"Email      : {teacher['email']}")
                print(f"Subject    : {teacher['subject']}")
                print(f"Class      : {teacher['class']}")
                print(f"Created At : {teacher['created_at']}")

                found = True

    else:
        print("Invalid Choice.")
        return

    if not found:
        print("Teacher Not Found.")

#def update_teacher(teachers):
    #pass
def update_teacher(teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    try:
        teacher_id = int(input("Enter Teacher ID to Update: "))
    except ValueError:
        print("Teacher ID must be an integer.")
        return

    for teacher in teachers:

        if teacher["teacher_id"] == teacher_id:

            print("\nCurrent Teacher Details")
            print("-" * 40)
            print(f"Name    : {teacher['name']}")
            print(f"Gender  : {teacher['gender']}")
            print(f"Phone   : {teacher['phone']}")
            print(f"Email   : {teacher['email']}")
            print(f"Subject : {teacher['subject']}")
            print(f"Class   : {teacher['class']}")

            name = input("Enter New Name: ").strip()
            gender = input("Enter New Gender: ").strip()
            phone = input("Enter New Phone Number: ").strip()
            email = input("Enter New Email: ").strip()

            if name == "":
                print("Name cannot be empty.")
                return

            if gender == "":
                print("Gender cannot be empty.")
                return

            if not phone.isdigit() or len(phone) != 10:
                print("Phone number must contain exactly 10 digits.")
                return

            if email == "":
                print("Email cannot be empty.")
                return

            # Duplicate Email Check
            for t in teachers:
                if (
                    t["teacher_id"] != teacher_id
                    and t["email"].lower() == email.lower()
                ):
                    print("Email already exists.")
                    return

            teacher["name"] = name
            teacher["gender"] = gender
            teacher["phone"] = phone
            teacher["email"] = email

            save_teachers(teachers)

            print("Teacher updated successfully.")
            return

    print("Teacher Not Found.")

#def delete_teacher(teachers):
    #pass
def delete_teacher(teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    try:
        teacher_id = int(input("Enter Teacher ID to Delete: "))
    except ValueError:
        print("Teacher ID must be an integer.")
        return

    for teacher in teachers:

        if teacher["teacher_id"] == teacher_id:

            print("\nTeacher Found")
            print("-" * 40)
            print(f"Teacher ID : {teacher['teacher_id']}")
            print(f"Name       : {teacher['name']}")
            print(f"Gender     : {teacher['gender']}")
            print(f"Phone      : {teacher['phone']}")
            print(f"Email      : {teacher['email']}")
            print(f"Subject    : {teacher['subject']}")
            print(f"Class      : {teacher['class']}")
            print(f"Created At : {teacher['created_at']}")

            confirm = input("\nAre you sure you want to delete this teacher? (Y/N): ").strip().upper()

            if confirm == "Y":
                teachers.remove(teacher)
                save_teachers(teachers)
                print("Teacher deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Teacher Not Found.")

#def assign_subject(subjects, teachers):
    #pass
def assign_subject(subjects, teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    if len(subjects) == 0:
        print("No Subject Record Found.")
        return

    print("\nAvailable Subjects")

    for subject in subjects:
        print("-" * 35)
        print(f"Subject Code : {subject['subject_code']}")
        print(f"Subject Name : {subject['subject_name']}")

    try:
        teacher_id = int(input("\nEnter Teacher ID: "))
    except ValueError:
        print("Teacher ID must be an integer.")
        return

    teacher = None

    for t in teachers:
        if t["teacher_id"] == teacher_id:
            teacher = t
            break

    if teacher is None:
        print("Teacher Not Found.")
        return

    subject_code = input("Enter Subject Code: ").strip().upper()

    for subject in subjects:

        if subject["subject_code"] == subject_code:

            teacher["subject"] = subject["subject_name"]

            save_teachers(teachers)

            print("Subject Assigned Successfully.")
            return

    print("Subject Not Found.")

#def assign_class(students, teachers):
    #pass
def assign_class(students, teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    if len(students) == 0:
        print("No Student Record Found.")
        return

    # Get unique classes from students
    classes = []

    for student in students:
        if student["grade"] not in classes:
            classes.append(student["grade"])

    print("\nAvailable Classes")
    print("-" * 35)

    for cls in classes:
        print(cls)

    try:
        teacher_id = int(input("\nEnter Teacher ID: "))
    except ValueError:
        print("Teacher ID must be an integer.")
        return

    teacher = None

    for t in teachers:
        if t["teacher_id"] == teacher_id:
            teacher = t
            break

    if teacher is None:
        print("Teacher Not Found.")
        return

    class_name = input("Enter Class: ").strip()

    if class_name not in classes:
        print("Class Not Found.")
        return

    teacher["class"] = class_name

    save_teachers(teachers)

    print("Class Assigned Successfully.")

#def teacher_report(teachers):
    #pass
def teacher_report(teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    print("\n========== Teacher Report ==========")
    print(f"Total Teachers : {len(teachers)}")

    count = 1

    for teacher in teachers:

        print(f"\nTeacher {count}")
        print("-" * 40)
        print(f"Teacher ID : {teacher['teacher_id']}")
        print(f"Name       : {teacher['name']}")
        print(f"Gender     : {teacher['gender']}")
        print(f"Phone      : {teacher['phone']}")
        print(f"Email      : {teacher['email']}")

        if teacher["subject"] == "":
            print("Subject    : Not Assigned")
        else:
            print(f"Subject    : {teacher['subject']}")

        if teacher["class"] == "":
            print("Class      : Not Assigned")
        else:
            print(f"Class      : {teacher['class']}")

        print(f"Created At : {teacher['created_at']}")

        count += 1

#def export_teachers_csv(teachers):
  #  pass
def export_teachers_csv(teachers):

    if len(teachers) == 0:
        print("No Teacher Record Found.")
        return

    try:
        with open("teachers.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Header
            writer.writerow([
                "Teacher ID",
                "Name",
                "Gender",
                "Phone",
                "Email",
                "Subject",
                "Class",
                "Created At"
            ])

            # Data
            for teacher in teachers:

                writer.writerow([
                    teacher["teacher_id"],
                    teacher["name"],
                    teacher["gender"],
                    teacher["phone"],
                    teacher["email"],
                    teacher["subject"],
                    teacher["class"],
                    teacher["created_at"]
                ])

        print("Teachers Exported Successfully.")

    except Exception as error:
        print(f"Error Exporting Teachers: {error}")

#def import_teachers_csv():
    #pass
def import_teachers_csv():

    teachers = []

    try:
        with open("teachers.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                teacher = {
                    "teacher_id": int(row["Teacher ID"]),
                    "name": row["Name"],
                    "gender": row["Gender"],
                    "phone": row["Phone"],
                    "email": row["Email"],
                    "subject": row["Subject"],
                    "class": row["Class"],
                    "created_at": row["Created At"]
                }

                teachers.append(teacher)

        save_teachers(teachers)

        print("Teachers Imported Successfully.")
        return teachers

    except FileNotFoundError:
        print("teachers.csv file not found.")
        return load_teachers()

    except Exception as error:
        print(f"Error Importing Teachers: {error}")
        return load_teachers()

# Menu
def teacher_menu():

    students = load_students()
    subjects = load_subjects()
    teachers = load_teachers()

    while True:

        print("\n===== Teacher Module =====")
        print("1. Add Teachers")
        print("2. View Teachers")
        print("3. Search Teacher")
        print("4. Update Teacher")
        print("5. Delete Teacher")
        print("6. Assign Subject")
        print("7. Assign Class")
        print("8. Teacher Report")
        print("9. Backup Teachers")
        print("10. Restore Teachers")
        print("11. CSV Export")
        print("12. CSV Import")
        print("13. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_teacher(teachers)

        elif choice == "2":
            view_teachers(teachers)

        elif choice == "3":
            search_teacher(teachers)

        elif choice == "4":
            update_teacher(teachers)

        elif choice == "5":
            delete_teacher(teachers)

        elif choice == "6":
            assign_subject(subjects, teachers)

        elif choice == "7":
            assign_class(students, teachers)

        elif choice == "8":
            teacher_report(teachers)

        elif choice == "9":
            backup_teachers()

        elif choice == "10":
            teachers = restore_teachers()

        elif choice == "11":
            export_teachers_csv(teachers)

        elif choice == "12":
            teachers = import_teachers_csv()

        elif choice == "13":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
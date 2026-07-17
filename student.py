#2. save to json
import json

#3.backup json data
import shutil

#4. csv - import/export
import csv

#add_student

def add_student(students):
    name = input("Enter Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    grade = input("Enter Grade: ").strip()

    try:
        rollno = int(input("Enter Roll No: "))
    except ValueError:
        print("Roll No must be an integer.")
        return

    # Duplicate Roll Number Check
    for student in students:
        if student["rollno"] == rollno:
            print("Roll Number already exists.")
            return

    student = {
        "name": name,
        "grade": grade,
        "rollno": rollno
    }

    students.append(student)
    save_students(students) #2.save json data (save data automatically)
    print("Student added successfully.")
    
#view_students

def view_students(students):

    if len(students) == 0:
        print("\nNo Student Record Found.\n")
        return

    print("\nStudent List")
    print("=" * 40)

    for index, student in enumerate(students, start=1):

        print(f"Student {index}")
        print("-" * 40)
        print(f"Name    : {student['name']}")
        print(f"Grade   : {student['grade']}")
        print(f"Roll No : {student['rollno']}")
        print()

#search_student

def search_student(students):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    print("\nSearch Student")
    print("1. Search by Roll No")
    print("2. Search by Name")

    choice = input("Enter choice: ")

    if choice == "1":

        try:
            rollno = int(input("Enter Roll No: "))
        except ValueError:
            print("Invalid Roll Number.")
            return

        for student in students:
            if student["rollno"] == rollno:
                print("\nStudent Found")
                print("-" * 35)
                print(f"Name    : {student['name']}")
                print(f"Grade   : {student['grade']}")
                print(f"Roll No : {student['rollno']}")
                return

        print("Student not found.")

    elif choice == "2":

        name = input("Enter Name: ").strip().lower()

        found = False

        for student in students:
            if student["name"].lower() == name:
                print("\nStudent Found")
                print("-" * 35)
                print(f"Name    : {student['name']}")
                print(f"Grade   : {student['grade']}")
                print(f"Roll No : {student['rollno']}")
                found = True

        if not found:
            print("Student not found.")

    else:
        print("Invalid Choice.")

#update_student

def update_student(students):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No to Update: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    for student in students:

        if student["rollno"] == rollno:

            print("\nStudent Found")
            print("-" * 35)
            print(f"Current Name    : {student['name']}")
            print(f"Current Grade   : {student['grade']}")
            print(f"Current Roll No : {student['rollno']}")

            print("\nEnter New Details")

            name = input("New Name: ").strip()
            grade = input("New Grade: ").strip()

            try:
                new_rollno = int(input("New Roll No: "))
            except ValueError:
                print("Invalid Roll Number.")
                return

            # Check duplicate roll number
            if new_rollno != rollno:
                for s in students:
                    if s["rollno"] == new_rollno:
                        print("Roll Number already exists.")
                        return

            student["name"] = name
            student["grade"] = grade
            student["rollno"] = new_rollno
            
            save_students(students) #2.save json data (save data automatically)
            
            print("Student Updated Successfully.")
            return
    print("Student not found.")

#delete_student

def delete_student(students):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    try:
        rollno = int(input("Enter Roll No to Delete: "))
    except ValueError:
        print("Invalid Roll Number.")
        return

    for student in students:

        if student["rollno"] == rollno:

            print("\nStudent Found")
            print("-" * 35)
            print(f"Name    : {student['name']}")
            print(f"Grade   : {student['grade']}")
            print(f"Roll No : {student['rollno']}")

            choice = input("\nAre you sure you want to delete? (Y/N): ").strip().upper()

            if choice == "Y":
                students.remove(student)

                save_students(students) #2.save json data (save data automatically) in add/update/delete

                print("Student Deleted Successfully.")
            else:
                print("Deletion Cancelled.")

            return

    print("Student not found.")

#sort_student

def sort_students(students):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    print("\nSort Students")
    print("1. Sort by Name")
    print("2. Sort by Grade")
    print("3. Sort by Roll Number")

    choice = input("Enter choice: ")

    if choice == "1":
        students.sort(key=lambda student: student["name"].lower())
        save_students(students) #2.save json data (save data automatically) in add/update/delete/sort
        print("Students sorted by Name.")

    elif choice == "2":
        students.sort(key=lambda student: student["grade"])
        save_students(students) #2.save json data (save data automatically) in add/update/delete/sort
        print("Students sorted by Grade.")

    elif choice == "3":
        students.sort(key=lambda student: student["rollno"])
        save_students(students) #2.save json data (save data automatically) in add/update/delete/sort
        print("Students sorted by Roll Number.")

    else:
        print("Invalid Choice.")
        return

    view_students(students)

#count_students

def count_students(students):

    total_students = len(students)

    print("\nStudent Count")
    print("-" * 30)
    print(f"Total Students : {total_students}")

#2. save to json
def save_students(students):
    try:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Students saved successfully.")

    except Exception as error:
        print(f"Error saving students: {error}")

#2.load from json
def load_students():

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        print("Students loaded successfully.")
        return students

    except FileNotFoundError:
        print("No saved student records found.")
        return []

    except json.JSONDecodeError:
        print("Error: students.json is empty or corrupted.")
        return []

    except Exception as error:
        print(f"Error loading students: {error}")
        return []

#3. backup json data
def backup_students():

    try:
        shutil.copy("students.json", "backup_students.json")
        print("Backup created successfully.")

    except FileNotFoundError:
        print("No student data found to backup.")

    except Exception as error:
        print(f"Error creating backup: {error}")

#3. restore json data
def restore_students():

    try:
        shutil.copy("backup_students.json", "students.json")
        print("Data restored successfully.")

        return load_students()

    except FileNotFoundError:
        print("Backup file not found.")
        return []

    except Exception as error:
        print(error)
        return []

#4. csv export
def export_csv(students):

    if len(students) == 0:
        print("No Student Record Found.")
        return

    try:
        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Header
            writer.writerow(["Name", "Grade", "Roll No"])

            # Student Data
            for student in students:
                writer.writerow([
                    student["name"],
                    student["grade"],
                    student["rollno"]
                ])

        print("Students exported successfully.")

    except Exception as error:
        print(f"Error exporting CSV: {error}")

#4. csv import (restore csv data)
def import_csv():

    students = []

    try:
        with open("students.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                student = {
                    "name": row["Name"],
                    "grade": row["Grade"],
                    "rollno": int(row["Roll No"])
                }

                students.append(student)

        save_students(students)

        print("Students imported successfully.")

        return students

    except FileNotFoundError:
        print("students.csv not found.")
        return load_students()

    except Exception as error:
        print(f"Error importing CSV: {error}")
        return load_students()

#5. student module menu selection 
#(shifting from main.py to here as now main will have module selection within that menu selection)
# main -> module -> menu
def student_menu():
    """
    students = []
    """
    students = load_students() #Now every time the program starts, it automatically loads previously saved data.

    while True:

        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Count Students")
        print("8. Save Students") ##2. save to json
        print("9. Backup Data") ##3. backup json data
        print("10. Restore Data") ##3. restore json data
        print("11. CSV Export") ##4. csv export
        print("12. CSV Import") ##4. csv import (restore csv data)
        print("13. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)
    
        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            sort_students(students)

        elif choice == "7":
            count_students(students)

        elif choice == "8": #2. save to json
            save_students(students)

        elif choice == "9":
            backup_students() #3. backup json data

        elif choice == "10":
            students = restore_students() #3. restore json data

        elif choice == "11":
            export_csv(students) #4. csv export

        elif choice == "12":
            students = import_csv() #4. csv import (restore csv data) 

        elif choice == "13":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

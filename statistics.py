import datetime
from student import load_students, save_students
from gpa import load_gpa
from teachers import load_teachers
from attendance import load_attendance
from marks import load_marks

def total_students(students):

    print("\n========== Total Students ==========")

    if len(students) == 0:
        print("No Student Records Found.")
        return

    print(f"Total Students : {len(students)}")

def total_teachers(teachers):

    print("\n========== Total Teachers ==========")

    if len(teachers) == 0:
        print("No Teacher Records Found.")
        return

    print(f"Total Teachers : {len(teachers)}")

def present_today(attendance):

    print("\n========== Present Today ==========")

    if len(attendance) == 0:
        print("No Attendance Records Found.")
        return

    today = str(datetime.date.today())
    present = 0

    for record in attendance:

        if (
            record["date"] == today and
            record["status"].lower() == "present"
        ):
            present += 1

    print(f"Present Students Today : {present}")

def absent_today(attendance):

    print("\n========== Absent Today ==========")

    if len(attendance) == 0:
        print("No Attendance Records Found.")
        return

    today = str(datetime.date.today())
    absent = 0

    for record in attendance:

        if (
            record["date"] == today and
            record["status"].lower() == "absent"
        ):
            absent += 1

    print(f"Absent Students Today : {absent}")

def highest_gpa(gpa):

    print("\n========== Highest GPA ==========")

    if len(gpa) == 0:
        print("No GPA Records Found.")
        return

    highest = gpa[0]

    for record in gpa:

        if record["gpa"] > highest["gpa"]:
            highest = record

    print(f"Roll No : {highest['rollno']}")
    print(f"GPA     : {highest['gpa']:.2f}")
    print(f"Grade   : {highest['grade']}")
    print(f"Date    : {highest['date']}")

def lowest_gpa(gpa):

    print("\n========== Lowest GPA ==========")

    if len(gpa) == 0:
        print("No GPA Records Found.")
        return

    lowest = gpa[0]

    for record in gpa:

        if record["gpa"] < lowest["gpa"]:
            lowest = record

    print(f"Roll No : {lowest['rollno']}")
    print(f"GPA     : {lowest['gpa']:.2f}")
    print(f"Grade   : {lowest['grade']}")
    print(f"Date    : {lowest['date']}")

def average_gpa(gpa):

    print("\n========== Average GPA ==========")

    if len(gpa) == 0:
        print("No GPA Records Found.")
        return

    total_gpa = 0

    for record in gpa:
        total_gpa += record["gpa"]

    average = total_gpa / len(gpa)

    print(f"Average GPA : {average:.2f}")

def highest_marks(marks):

    print("\n========== Highest Marks ==========")

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    highest = marks[0]
    highest_total = sum(highest["subjects"].values())

    for record in marks:

        total = sum(record["subjects"].values())

        if total > highest_total:
            highest = record
            highest_total = total

    print(f"Roll No     : {highest['rollno']}")

    print("\nSubject-wise Marks")
    print("-" * 30)

    for subject, mark in highest["subjects"].items():
        print(f"{subject:<10}: {mark}")

    print("-" * 30)
    print(f"Total Marks : {highest_total}")

def subject_statistics(marks):

    print("\n========== Subject Statistics ==========")

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    subjects = marks[0]["subjects"].keys()

    for subject in subjects:

        subject_marks = []

        for record in marks:
            subject_marks.append(record["subjects"][subject])

        highest = max(subject_marks)
        lowest = min(subject_marks)
        average = sum(subject_marks) / len(subject_marks)

        print(f"\n{subject}")
        print("-" * 30)
        print(f"Highest Marks : {highest}")
        print(f"Lowest Marks  : {lowest}")
        print(f"Average Marks : {average:.2f}")

# Menu
def statistics_menu():

    students = load_students()
    teachers = load_teachers()
    gpa = load_gpa()
    attendance = load_attendance()
    marks = load_marks()

    while True:

        print("\n===== Statistics Module =====")
        print("1. Total Students")
        print("2. Total Teachers")
        print("3. Present Today")
        print("4. Absent Today")
        print("5. Highest GPA")
        print("6. Lowest GPA")
        print("7. Average GPA")
        print("8. Highest Marks")
        print("9. Subject Statistics")
        print("10. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            total_students(students)

        elif choice == "2":
            total_teachers(teachers)

        elif choice == "3":
            present_today(attendance)

        elif choice == "4":
            absent_today(attendance)

        elif choice == "5":
            highest_gpa(gpa)

        elif choice == "6":
            lowest_gpa(gpa)

        elif choice == "7":
            average_gpa(gpa)

        elif choice == "8":
            highest_marks(marks)

        elif choice == "9":
            subject_statistics(marks)

        elif choice == "10":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
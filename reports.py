from student import load_students
from attendance import load_attendance
from marks import load_marks
from teachers import load_teachers
from gpa import load_gpa

def student_report(students):

    print("\n========== Student Report ==========")

    if len(students) == 0:
        print("No Student Records Found.")
        return

    print(f"Total Students : {len(students)}")
    print("-" * 70)

    print(f"{'S.No':<6}{'Roll No':<10}{'Name':<25}{'Grade':<10}")
    print("-" * 70)

    for index, student in enumerate(students, start=1):
        print(
            f"{index:<6}"
            f"{student['rollno']:<10}"
            f"{student['name']:<25}"
            f"{student['grade']:<10}"
        )

    print("-" * 70)

def attendance_report(attendance):
    pass

def marks_report(marks):
    pass

def gpa_report(gpa):
    pass

def teacher_report(teachers):
    pass

def export_report(students, attendance, marks, gpa, teachers):
    pass

def reports_menu():

    while True:

        print("\n===== Reports Module =====")
        print("1. Student Report")
        print("2. Attendance Report")
        print("3. Marks Report")
        print("4. GPA Report")
        print("5. Teacher Report")
        print("6. Export Report")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            student_report(load_students())

        elif choice == "2":
            attendance_report(load_attendance())

        elif choice == "3":
            marks_report(load_marks())

        elif choice == "4":
            gpa_report(load_gpa())

        elif choice == "5":
            teacher_report(load_teachers())

        elif choice == "6":
            export_report(
                load_students(),
                load_attendance(),
                load_marks(),
                load_gpa(),
                load_teachers()
            )

        elif choice == "7":
            print("Thank You")
            break

        else:
            print("Invalid Choice")
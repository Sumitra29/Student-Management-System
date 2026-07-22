from student import student_menu
from attendance import attendance_menu
from marks import marks_menu
from gpa import gpa_menu
from subjects import subject_menu
from teachers import teacher_menu
from users import authentication_menu
from system_logs import logging_menu
from reports import reports_menu
from statistics import statistics_menu

while True:
    print("\n===== Student Management System =====")
    print("1. Student Module")
    print("2. Attendance Module")
    print("3. Marks Module")
    print("4. GPA Module")
    print("5. Subject Module")
    print("6. Teacher Module")
    print("7. Authentication Module")
    print("8. Logging Module")
    print("9. Reports Module")
    print("10. Statistics Module")
    print("11. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        student_menu()

    elif choice == "2":
        attendance_menu()

    elif choice == "3":
        marks_menu()

    elif choice == "4":
        gpa_menu()

    elif choice == "5":
        subject_menu()

    elif choice == "6":
        teacher_menu()

    elif choice == "7":
        authentication_menu()

    elif choice == "8":
        logging_menu()

    elif choice == "9":
        reports_menu()

    elif choice == "10":
        statistics_menu()

    elif choice == "11":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
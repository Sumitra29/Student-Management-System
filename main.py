from student import student_menu
from attendance import attendance_menu
from marks import marks_menu
from gpa import gpa_menu
while True:
    print("\n===== Student Management System =====")
    print("1. Student Module")
    print("2. Attendance Module")
    print("3. Marks Module")
    print("4. GPA Module")
    print("5. Exit")

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
        print("Thank You")
        break

    else:
        print("Invalid Choice")
from student import student_menu
from attendance import attendance_menu

while True:
    print("\n===== Student Management System =====")
    print("1. Student Module")
    print("2. Attendance Module")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        student_menu()

    elif choice == "2":
        attendance_menu()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
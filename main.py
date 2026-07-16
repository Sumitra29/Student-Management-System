from student import *

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
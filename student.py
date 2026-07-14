def add_student(students):
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    rollno = int(input("Enter Roll No: "))
    student = {
        "name" : name,
        "grade" : grade,
        "rollno" : rollno
    }
    students.append(student)

def view_students(students):
    if len(students) == 0:
        print("No student Record")
    count = 1

    for student in students:
        print(f"Total Student {count}")
        print("-"*35)
        print(f"Name: {student['name']}")
        print(f"Grade: {student['grade']}")
        print(f"Roll No: {student['rollno']}")
        count += 1


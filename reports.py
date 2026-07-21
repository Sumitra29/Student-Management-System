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

    print("\n========== Attendance Report ==========")

    if len(attendance) == 0:
        print("No Attendance Records Found.")
        return

    present = 0
    absent = 0

    for record in attendance:
        if record["status"].lower() == "present":
            present += 1
        elif record["status"].lower() == "absent":
            absent += 1

    total = len(attendance)
    percentage = (present / total) * 100

    print(f"Total Records      : {total}")
    print(f"Present Students   : {present}")
    print(f"Absent Students    : {absent}")
    print(f"Attendance Percent : {percentage:.2f}%")

    print("-" * 75)
    print(f"{'S.No':<6}{'Roll No':<10}{'Date':<15}{'Status':<10}")
    print("-" * 75)

    for index, record in enumerate(attendance, start=1):
        print(
            f"{index:<6}"
            f"{record['rollno']:<10}"
            f"{record['date']:<15}"
            f"{record['status']:<10}"
        )

    print("-" * 75)

def marks_report(marks):

    print("\n========== Marks Report ==========")

    if len(marks) == 0:
        print("No Marks Records Found.")
        return

    highest_total = 0
    lowest_total = sum(marks[0]["subjects"].values())
    grand_total = 0

    print(f"Total Students : {len(marks)}")
    print("-" * 85)
    print(f"{'S.No':<6}{'Roll No':<10}{'Python':<10}{'Math':<10}{'English':<10}{'Total':<10}{'Average'}")
    print("-" * 85)

    for index, record in enumerate(marks, start=1):

        python = record["subjects"]["Python"]
        math = record["subjects"]["Math"]
        english = record["subjects"]["English"]

        total = python + math + english
        average = total / 3

        grand_total += total

        if total > highest_total:
            highest_total = total

        if total < lowest_total:
            lowest_total = total

        print(
            f"{index:<6}"
            f"{record['rollno']:<10}"
            f"{python:<10}"
            f"{math:<10}"
            f"{english:<10}"
            f"{total:<10}"
            f"{average:.2f}"
        )

    overall_average = grand_total / len(marks)

    print("-" * 85)
    print(f"Highest Total   : {highest_total}")
    print(f"Lowest Total    : {lowest_total}")
    print(f"Average Total   : {overall_average:.2f}")

def gpa_report(gpa):

    print("\n========== GPA Report ==========")

    if len(gpa) == 0:
        print("No GPA Records Found.")
        return

    highest_gpa = gpa[0]["gpa"]
    lowest_gpa = gpa[0]["gpa"]
    total_gpa = 0

    print(f"Total Students : {len(gpa)}")
    print("-" * 75)
    print(f"{'S.No':<6}{'Roll No':<10}{'GPA':<10}{'Grade':<10}{'Date'}")
    print("-" * 75)

    for index, record in enumerate(gpa, start=1):

        current_gpa = record["gpa"]
        total_gpa += current_gpa

        if current_gpa > highest_gpa:
            highest_gpa = current_gpa

        if current_gpa < lowest_gpa:
            lowest_gpa = current_gpa

        print(
            f"{index:<6}"
            f"{record['rollno']:<10}"
            f"{current_gpa:<10.2f}"
            f"{record['grade']:<10}"
            f"{record['date']}"
        )

    average_gpa = total_gpa / len(gpa)

    print("-" * 75)
    print(f"Highest GPA : {highest_gpa:.2f}")
    print(f"Lowest GPA  : {lowest_gpa:.2f}")
    print(f"Average GPA : {average_gpa:.2f}")

def teacher_report(teachers):

    print("\n========== Teacher Report ==========")

    if len(teachers) == 0:
        print("No Teacher Records Found.")
        return

    print(f"Total Teachers : {len(teachers)}")
    print("-" * 120)

    print(
        f"{'S.No':<6}"
        f"{'ID':<8}"
        f"{'Name':<25}"
        f"{'Gender':<10}"
        f"{'Phone':<15}"
        f"{'Subject':<20}"
        f"{'Class'}"
    )

    print("-" * 120)

    for index, teacher in enumerate(teachers, start=1):

        print(
            f"{index:<6}"
            f"{teacher['teacher_id']:<8}"
            f"{teacher['name']:<25}"
            f"{teacher['gender']:<10}"
            f"{teacher['phone']:<15}"
            f"{teacher['subject']:<20}"
            f"{teacher['class']}"
        )

    print("-" * 120)

def export_report(students, attendance, marks, gpa, teachers):

    try:
        with open("school_report.txt", "w") as file:

            file.write("=========================================\n")
            file.write("     STUDENT MANAGEMENT SYSTEM REPORT\n")
            file.write("=========================================\n\n")

            # Student Report
            file.write("STUDENT REPORT\n")
            file.write("------------------------------\n")
            file.write(f"Total Students : {len(students)}\n\n")

            # Attendance Report
            present = 0
            absent = 0

            for record in attendance:
                if record["status"].lower() == "present":
                    present += 1
                else:
                    absent += 1

            file.write("ATTENDANCE REPORT\n")
            file.write("------------------------------\n")
            file.write(f"Total Records : {len(attendance)}\n")
            file.write(f"Present       : {present}\n")
            file.write(f"Absent        : {absent}\n\n")

            # Marks Report
            highest_total = 0
            lowest_total = 0
            average_total = 0

            if len(marks) > 0:

                totals = []

                for record in marks:
                    total = sum(record["subjects"].values())
                    totals.append(total)

                highest_total = max(totals)
                lowest_total = min(totals)
                average_total = sum(totals) / len(totals)

            file.write("MARKS REPORT\n")
            file.write("------------------------------\n")
            file.write(f"Highest Total : {highest_total}\n")
            file.write(f"Lowest Total  : {lowest_total}\n")
            file.write(f"Average Total : {average_total:.2f}\n\n")

            # GPA Report
            highest_gpa = 0
            lowest_gpa = 0
            average_gpa = 0

            if len(gpa) > 0:

                gpas = [record["gpa"] for record in gpa]

                highest_gpa = max(gpas)
                lowest_gpa = min(gpas)
                average_gpa = sum(gpas) / len(gpas)

            file.write("GPA REPORT\n")
            file.write("------------------------------\n")
            file.write(f"Highest GPA : {highest_gpa:.2f}\n")
            file.write(f"Lowest GPA  : {lowest_gpa:.2f}\n")
            file.write(f"Average GPA : {average_gpa:.2f}\n\n")

            # Teacher Report
            file.write("TEACHER REPORT\n")
            file.write("------------------------------\n")
            file.write(f"Total Teachers : {len(teachers)}\n\n")

        print("School Report Exported Successfully.")

    except Exception as error:
        print(f"Error Exporting Report : {error}")

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
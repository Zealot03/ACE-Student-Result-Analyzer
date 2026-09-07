def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def enter_students():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\nStudent", i + 1)

        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        grade = get_grade(marks)
        student = {
            "name": name,
            "marks": marks,
            "grade": grade
        }
        students.append(student)
    return students

def calculate_result(students):
    total = 0
    passed = 0
    failed = 0
    highest = students[0]
    lowest = students[0]

    for student in students:
        total = total + student["marks"]

        if student["marks"] >= 50:
            passed = passed + 1
        else:
            failed = failed + 1

        if student["marks"] > highest["marks"]:
            highest = student

        if student["marks"] < lowest["marks"]:
            lowest = student

    average = total / len(students)
    pass_percentage = (passed / len(students)) * 100

    print("\n========== CLASS RESULT ==========")
    print("\nName\tMarks\tGrade")

    for student in students:
        print(
            student["name"],
            "\t",
            student["marks"],
            "\t",
            student["grade"]
        )

    print("\nClass Average:", round(average, 2))
    print("Highest:", highest["name"], "-", highest["marks"])
    print("Lowest:", lowest["name"], "-", lowest["marks"])
    print("Students Passed:", passed)
    print("Students Failed:", failed)
    print("Pass Percentage:", round(pass_percentage, 2), "%")

def save_file(students):
    file = open("student_results.txt", "w")
    file.write("STUDENT RESULT REPORT\n")
    file.write("=====================\n\n")

    for student in students:
        file.write(
            student["name"] + " - " +
            str(student["marks"]) + " - " +
            student["grade"] + "\n"
        )
    file.close()
    print("\nResults saved in student_results.txt")

print("===== STUDENT RESULT ANALYZER =====")
students = enter_students()
calculate_result(students)
choice = input("\nDo you want to save the results? (yes/no): ")
if choice.lower() == "yes":
    save_file(students)
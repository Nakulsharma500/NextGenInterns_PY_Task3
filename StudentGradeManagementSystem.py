# Student Grade Management System

students = {}

def add_student():
    print("\nAdding a new student...")
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    students[student_id] = {
        'name': name,
        'grades': []
    }
    print(f"Student {name} with ID {student_id} added successfully.")

def record_grade():
    print("\nRecording student grade...")
    student_id = input("Enter student ID: ")
    if student_id in students:
        subject = input("Enter subject name: ")
        grade = float(input("Enter grade: "))
        students[student_id]['grades'].append({
            'subject': subject,
            'grade': grade
        })
        print(f"Grade recorded for {students[student_id]['name']} in {subject}.")
    else:
        print("Student not found.")

def calculate_average_grade(student_id):
    if student_id in students:
        grades = students[student_id]['grades']
        if grades:
            total_grades = sum(grade['grade'] for grade in grades)
            average_grade = total_grades / len(grades)
            return average_grade
        else:
            return 0
    else:
        return None

def display_student_info():
    print("\nDisplaying student information...")
    student_id = input("Enter student ID: ")
    if student_id in students:
        student = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print("Grades:")
        for grade in student['grades']:
            print(f"- {grade['subject']}: {grade['grade']}")
        average_grade = calculate_average_grade(student_id)
        if average_grade is not None:
            print(f"Average Grade: {average_grade}")
        else:
            print("No grades recorded yet.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add New Student")
        print("2. Record Student Grade")
        print("3. Display Student Information")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            record_grade()
        elif choice == '3':
            display_student_info()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

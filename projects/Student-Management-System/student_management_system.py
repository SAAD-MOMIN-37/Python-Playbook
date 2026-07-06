students = [
    {
        "roll_no": 101,
        "name": "Saad",
        "age": 21,
        "course": "AI",
        "marks": 95
    },
    {
        "roll_no": 102,
        "name": "Ali",
        "age": 20,
        "course": "ML",
        "marks": 88
    },
    {
        "roll_no": 103,
        "name": "Ahmed",
        "age": 22,
        "course": "Data Science",
        "marks": 91
    }
]

def add_students():
    roll_no = int(input("Enter roll number :"))
    name = input("Enter name :")
    age = int(input("Enter age :"))
    course = input("Enter course :")
    marks = int(input("Enter marks :"))
    student = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }
    for existing_student in students:
        if existing_student  == existing_student["roll_no"]:
            print(f"Student with Roll No {roll_no} already exists.")
            return
        
    students.append(student)
    print("-"*70)
    print("✅Student added Successfully!!")

# add_students()

def display_students():
    if not students:
        print("No students Found!!")
        return
    for student in students:
        print("-"*70)
        print(f'Roll No : {student["roll_no"]}')
        print(f'Name    : {student["name"]}')
        print(f'Age     : {student["age"]}')
        print(f'Course  : {student["course"]}')
        print(f'Marks   : {student["marks"]}')
        print("-"*70)

# display_students()

def search_students():
    rollno = int(input("Enter Roll No"))
    if not students:
        print("No students Found!!")
        return
    
    for student in students:
        if rollno == student["roll_no"]:
            print("-"*70)
            print(f'Roll No : {student["roll_no"]}')
            print(f'Name    : {student["name"]}')
            print(f'Age     : {student["age"]}')
            print(f'Course  : {student["course"]}')
            print(f'Marks   : {student["marks"]}')
            print("-"*70)
    
            return
            
    print("-"*70)
    print("Student Not Found!!")
    print("-"*70)
    return

# search_students()

def update_students():
    rollno = int(input("Enter Roll No"))
    if not students:
        print("No students Found!!")
        return
    
    for student in students:
        if rollno == student["roll_no"]:
            print("-"*70)
            print(f"Before update")
            print("-"*70)
            print(f'Roll No : {student["roll_no"]}')
            print(f'Name    : {student["name"]}')
            print(f'Age     : {student["age"]}')
            print(f'Course  : {student["course"]}')
            print(f'Marks   : {student["marks"]}')
            print("-"*70)

            student["name"] = input("Enter new name :")
            student["age"] = int(input("Enter new age :"))
            student["course"] = input("Enter new course :")
            student["marks"] = int(input("Enter new marks :"))
            
            print("-"*70)
            print(f"After update")
            print("-"*70)
            print(f'Roll No : {student["roll_no"]}')
            print(f'Name    : {student["name"]}')
            print(f'Age     : {student["age"]}')
            print(f'Course  : {student["course"]}')
            print(f'Marks   : {student["marks"]}')
            print("-"*70)
    
            return
            
    print("-"*70)
    print("Student Not Found!!")
    print("-"*70)
    return

# update_students()

def delete_students():
    rollno = int(input("Enter Roll No: "))

    if not students:
        print("No students found!")
        return

    for student in students:
        if rollno == student["roll_no"]:

            print("-" * 70)
            print("Student Information to Delete")
            print("-" * 70)
            print(f'Roll No : {student["roll_no"]}')
            print(f'Name    : {student["name"]}')
            print(f'Age     : {student["age"]}')
            print(f'Course  : {student["course"]}')
            print(f'Marks   : {student["marks"]}')
            print("-" * 70)

            confirm = input("Are you sure you want to delete this student? (y/n): ").lower()

            if confirm in ["y", "yes"]:
                students.remove(student)
                print("-" * 70)
                print(f'✅ Student "{student["name"]}" deleted successfully!')
                print("-" * 70)
            else:
                print("-" * 70)
                print("❌ Deletion cancelled.")
                print("-" * 70)

            return

    print("-" * 70)
    print("Student not found!")
    print("-" * 70)

# delete_students()

import json
def save_students(file = "students.json"):
    with open(file, "w") as f:
        json.dump(students,f,indent =4)
    print("✅ Students saved successfully!")

save_students()

import json

def load_students(file="students.json"):
    global students

    with open(file, "r") as f:
        students = json.load(f)

    print("✅ Students loaded successfully!")

load_students()

def system():
    
    load_students()

    while True:

        print("=" * 70)
        print("STUDENT MANAGEMENT SYSTEM")
        print("=" * 70)

        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Student")
        print("7. Exit")

        print("=" * 70)

        try:
            choice = int(input("Enter your choice (1-7): "))
            print("=" * 70)

            if choice == 1:
                add_students()

            elif choice == 2:
                display_students()

            elif choice == 3:
                search_students()

            elif choice == 4:
                update_students()

            elif choice == 5:
                delete_students()

            elif choice == 6:
                save_students()

            elif choice == 7:
                save_students()
                print("-" * 70)
                print("Thank you for using Student Management System!")
                print("-" * 70)
                break

            else:
                print("❌ Please enter a number between 1 and 7.")

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

system()
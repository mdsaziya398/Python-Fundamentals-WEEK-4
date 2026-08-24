
# STUDENT MANAGEMENT SYSTEM


# Import datetime library
# Purpose: Used to display the current date and time.
import datetime



# DATA STRUCTURE

# List used to store student records
students = []



# FILE HANDLING


FILE_NAME = "students.txt"


def load_students():
    """
    Read student records from the file when the program starts.
    """

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                student = {
                    "id": data[0],
                    "name": data[1],
                    "age": int(data[2]),
                    "marks": float(data[3])
                }

                students.append(student)

        file.close()

    except FileNotFoundError:
        # If the file does not exist, create it.
        file = open(FILE_NAME, "w")
        file.close()

    except ValueError:
        print("Error: Invalid data found in the file.")


def save_students():
    """
    Save all student records to the file.
    """

    file = open(FILE_NAME, "w")

    for student in students:
        file.write(
            student["id"] + "," +
            student["name"] + "," +
            str(student["age"]) + "," +
            str(student["marks"]) + "\n"
        )

    file.close()



# ADD STUDENT


def add_student():

    print("\n========== ADD STUDENT ==========")

    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        # Validate age
        if age <= 0:
            print("Error: Age must be greater than 0.")
            return

        # Validate marks
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return

        # Check whether ID already exists
        for student in students:
            if student["id"] == student_id:
                print("Error: Student ID already exists.")
                return

        # Create dictionary for student
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "marks": marks
        }

        # Add student to list
        students.append(student)

        # Save to file
        save_students()

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter valid numbers for age and marks.")


# VIEW STUDENTS

def view_students():

    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    print("ID\tName\t\tAge\tMarks")
    print("------------------------------------------")

    # Loop through all students
    for student in students:
        print(
            student["id"], "\t",
            student["name"], "\t\t",
            student["age"], "\t",
            student["marks"]
        )



# SEARCH STUDENT


def search_student():

    print("\n========== SEARCH STUDENT ==========")

    search_id = input("Enter Student ID: ")

    found = False

    # Search using loop
    for student in students:

        if student["id"] == search_id:

            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

            found = True
            break

    if not found:
        print("Student not found.")



# UPDATE STUDENT


def update_student():

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID to update: ")

    for student in students:

        if student["id"] == student_id:

            try:
                new_name = input("Enter New Name: ")
                new_age = int(input("Enter New Age: "))
                new_marks = float(input("Enter New Marks: "))

                if new_age <= 0:
                    print("Error: Age must be greater than 0.")
                    return

                if new_marks < 0 or new_marks > 100:
                    print("Error: Marks must be between 0 and 100.")
                    return

                student["name"] = new_name
                student["age"] = new_age
                student["marks"] = new_marks

                save_students()

                print("Student details updated successfully!")
                return

            except ValueError:
                print("Error: Please enter valid age and marks.")

    print("Student not found.")



# DELETE STUDENT


def delete_student():

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID to delete: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")



# DISPLAY CURRENT DATE AND TIME


def display_datetime():

    current_time = datetime.datetime.now()

    print("\nCurrent Date and Time:", current_time)



# MAIN MENU


def main():

    # Load existing records from file
    load_students()

    print("\n==========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("==========================================")

    display_datetime()

    # Infinite loop for menu
    while True:

        print("\n-------------- MENU ----------------")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("------------------------------------")

        try:
            choice = int(input("Enter your choice (1-6): "))

            # Conditional statements
            if choice == 1:
                add_student()

            elif choice == 2:
                view_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_student()

            elif choice == 5:
                delete_student()

            elif choice == 6:
                print("\nThank you for using Student Management System!")
                break

            else:
                print("Invalid choice! Please select between 1 and 6.")

        except ValueError:
            print("Error: Please enter a number between 1 and 6.")



# PROGRAM START
if __name__ == "__main__":
    main()
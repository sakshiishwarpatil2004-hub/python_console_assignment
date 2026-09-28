"""
Student Record Management System
--------------------------------
Author: Sakshi Ishwar Patil
Roll No.: 150097926022
Course: MCA
Subject: Python Programming

A menu-driven console application for managing student records.
The program demonstrates Python fundamentals such as variables,
lists, dictionaries, conditions, loops, functions, exception
handling, validation, and JSON file handling.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "records.json")


# ------------------------------------------------------------
# File Handling
# ------------------------------------------------------------

def load_records():
    """Load student records from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: records.json is invalid or corrupted.")
        print("Starting with an empty record list.")
        return []
    except OSError as error:
        print(f"Error reading data file: {error}")
        return []


def save_records(records):
    """Save all student records to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        return True
    except OSError as error:
        print(f"Error saving data: {error}")
        return False


# ------------------------------------------------------------
# Validation Functions
# ------------------------------------------------------------

def is_valid_email(email):
    """Return True if the email format looks valid."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    """Return True if the phone number contains exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def get_non_empty_input(prompt):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_semester(prompt):
    """Accept only semester values from 1 to 6."""
    while True:
        value = input(prompt).strip()

        try:
            semester = int(value)
            if 1 <= semester <= 6:
                return semester
            print("Semester must be between 1 and 6.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_email(prompt):
    """Keep asking until a valid email is entered."""
    while True:
        email = input(prompt).strip()
        if is_valid_email(email):
            return email
        print("Invalid email format. Example: student@example.com")


def get_valid_phone(prompt):
    """Keep asking until a valid 10-digit phone number is entered."""
    while True:
        phone = input(prompt).strip()
        if is_valid_phone(phone):
            return phone
        print("Phone number must contain exactly 10 digits.")


def get_valid_marks(prompt):
    """Accept marks only from 0 to 100."""
    while True:
        value = input(prompt).strip()

        try:
            marks = float(value)
            if 0 <= marks <= 100:
                return round(marks, 2)
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def get_next_student_id(records):
    """Generate IDs in the format S001, S002, S003, ..."""
    if not records:
        return "S001"

    numbers = []

    for record in records:
        student_id = str(record.get("student_id", ""))

        if student_id.startswith("S") and student_id[1:].isdigit():
            numbers.append(int(student_id[1:]))

    next_number = max(numbers, default=0) + 1
    return f"S{next_number:03d}"


def find_student_by_id(records, student_id):
    """Find one student using exact Student ID."""
    student_id = student_id.strip().upper()

    for record in records:
        if record.get("student_id", "").upper() == student_id:
            return record

    return None


def print_student(record):
    """Display one student record in a readable format."""
    print("-" * 52)
    print(f"Student ID : {record['student_id']}")
    print(f"Name       : {record['name']}")
    print(f"Course     : {record['course']}")
    print(f"Semester   : {record['semester']}")
    print(f"Email      : {record['email']}")
    print(f"Phone      : {record['phone']}")
    print(f"Marks      : {record['marks']}")


# ------------------------------------------------------------
# CRUD Operations
# ------------------------------------------------------------

def add_student(records):
    """Add a new student record."""
    print("\n--- Add Student ---")

    student = {
        "student_id": get_next_student_id(records),
        "name": get_non_empty_input("Enter student name: "),
        "course": get_non_empty_input("Enter course: "),
        "semester": get_valid_semester("Enter semester (1-6): "),
        "email": get_valid_email("Enter email: "),
        "phone": get_valid_phone("Enter 10-digit phone number: "),
        "marks": get_valid_marks("Enter marks (0-100): ")
    }

    records.append(student)

    if save_records(records):
        print(f"Student added successfully with ID {student['student_id']}.")
    else:
        print("Student was added in memory but could not be saved.")


def view_students(records):
    """Display all student records."""
    print("\n--- All Student Records ---")

    if not records:
        print("No student records found.")
        return

    for record in records:
        print_student(record)

    print("-" * 52)
    print(f"Total students: {len(records)}")


def search_student(records):
    """Search students by ID or partial/full name."""
    print("\n--- Search Student ---")
    print("1. Search by Student ID")
    print("2. Search by Name")

    choice = input("Enter your choice (1-2): ").strip()

    if choice == "1":
        student_id = input("Enter Student ID: ").strip()
        student = find_student_by_id(records, student_id)

        if student:
            print("\nStudent found:")
            print_student(student)
        else:
            print("No student found with that ID.")

    elif choice == "2":
        query = input("Enter full or partial name: ").strip().lower()

        matches = [
            record
            for record in records
            if query in record.get("name", "").lower()
        ]

        if matches:
            print(f"\n{len(matches)} matching record(s) found:")
            for record in matches:
                print_student(record)
        else:
            print("No matching student found.")

    else:
        print("Invalid search option.")


def update_student(records):
    """Update an existing student record."""
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID to update: ").strip()
    student = find_student_by_id(records, student_id)

    if not student:
        print("No student found with that ID.")
        return

    print("\nCurrent details:")
    print_student(student)
    print("\nLeave any field blank to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    semester = input(f"Semester [{student['semester']}]: ").strip()
    email = input(f"Email [{student['email']}]: ").strip()
    phone = input(f"Phone [{student['phone']}]: ").strip()
    marks = input(f"Marks [{student['marks']}]: ").strip()

    if name:
        student["name"] = name

    if course:
        student["course"] = course

    if semester:
        try:
            semester_value = int(semester)
            if 1 <= semester_value <= 6:
                student["semester"] = semester_value
            else:
                print("Invalid semester. Previous value kept.")
        except ValueError:
            print("Invalid semester. Previous value kept.")

    if email:
        if is_valid_email(email):
            student["email"] = email
        else:
            print("Invalid email. Previous value kept.")

    if phone:
        if is_valid_phone(phone):
            student["phone"] = phone
        else:
            print("Invalid phone number. Previous value kept.")

    if marks:
        try:
            marks_value = float(marks)
            if 0 <= marks_value <= 100:
                student["marks"] = round(marks_value, 2)
            else:
                print("Marks must be between 0 and 100. Previous value kept.")
        except ValueError:
            print("Invalid marks. Previous value kept.")

    if save_records(records):
        print("Student record updated successfully.")
    else:
        print("Changes were made in memory but could not be saved.")


def delete_student(records):
    """Delete a student after confirmation."""
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID to delete: ").strip()
    student = find_student_by_id(records, student_id)

    if not student:
        print("No student found with that ID.")
        return

    print("\nStudent selected:")
    print_student(student)

    confirmation = input("\nAre you sure you want to delete this student? (y/n): ").strip().lower()

    if confirmation == "y":
        records.remove(student)

        if save_records(records):
            print("Student record deleted successfully.")
        else:
            print("Record was deleted in memory but could not be saved.")
    else:
        print("Delete operation cancelled.")


# ------------------------------------------------------------
# Statistics
# ------------------------------------------------------------

def show_statistics(records):
    """Display simple statistics based on student marks."""
    print("\n--- Student Statistics ---")

    if not records:
        print("No records available.")
        return

    marks_list = [float(record["marks"]) for record in records]

    highest = max(records, key=lambda record: float(record["marks"]))
    lowest = min(records, key=lambda record: float(record["marks"]))
    average = sum(marks_list) / len(marks_list)

    print(f"Total Students : {len(records)}")
    print(f"Average Marks  : {average:.2f}")
    print(f"Highest Marks  : {highest['marks']} ({highest['name']})")
    print(f"Lowest Marks   : {lowest['marks']} ({lowest['name']})")


# ------------------------------------------------------------
# Menu and Main Program
# ------------------------------------------------------------

def display_menu():
    """Display the main application menu."""
    print("\n" + "=" * 52)
    print("        STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 52)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")
    print("=" * 52)


def main():
    """Start the application and keep showing the menu until exit."""
    records = load_records()

    print("\nWelcome to the Student Record Management System")
    print("Created by Sakshi Ishwar Patil | MCA | Roll No. 150097926022")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                add_student(records)
            elif choice == "2":
                view_students(records)
            elif choice == "3":
                search_student(records)
            elif choice == "4":
                update_student(records)
            elif choice == "5":
                delete_student(records)
            elif choice == "6":
                show_statistics(records)
            elif choice == "7":
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

        except KeyboardInterrupt:
            print("\nOperation interrupted. Returning to main menu.")
        except Exception as error:
            print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
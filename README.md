# Student Record Management System

A menu-driven Python mini-project for managing student records.

## Student Details

- **Name:** Sakshi Ishwar Patil
- **Roll No.:** 150097926022
- **Course:** Masters of Computer Applications (MCA)
- **Subject:** Python Programming
- **Project Type:** Assignment - 1

## Project Description

The Student Record Management System is a console-based Python application that allows a user to manage student information using a simple menu.

The program supports adding, viewing, searching, updating and deleting student records. It also provides basic statistics such as average marks, highest marks and lowest marks.

Student information is stored in a local `records.json` file so that the data remains available even after the application is closed.

## Features

1. Add a new student
2. View all student records
3. Search by Student ID
4. Search by full or partial name
5. Update student information
6. Delete a student after confirmation
7. Display student statistics
8. Automatic Student ID generation
9. Email, phone, semester and marks validation
10. JSON-based persistent storage
11. Exception handling for invalid input and file errors

## Python Concepts Used

- Variables and data types
- Strings, integers and floating-point values
- Lists
- Dictionaries
- `if`, `elif`, `else`
- `for` loops
- `while` loops
- Functions
- File handling
- JSON
- Exception handling
- Regular expressions
- List comprehensions
- Lambda functions
- CRUD operations
- Input validation

## Project Structure

```text
student_record_management_ankit/
│
├── record_manager.py
├── records.json
├── README.md
└── Assignment_Report.md
```

## Record Format

Each student is stored as a dictionary such as:

```json
{
    "student_id": "S010",
    "name": "Ankit Sachin Kulkarni",
    "course": "MCA",
    "semester": 1,
    "email": "ankit.kulkarni@example.com",
    "phone": "9000000010",
    "marks": 87
}
```

> The contact details and marks included in the sample data are demonstration values only.

## How to Run

### Requirement

Python 3.7 or later.

No external library is required.

### Steps

1. Keep `record_manager.py` and `records.json` in the same folder.
2. Open Terminal / Command Prompt in that folder.
3. Run:

```bash
python3 record_manager.py
```

On Windows, you may also use:

```bash
python record_manager.py
```

## Main Menu

```text
====================================================
        STUDENT RECORD MANAGEMENT SYSTEM
====================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Statistics
7. Exit
====================================================
```

## Program Flow

```text
Start
  ↓
Load records.json
  ↓
Display Main Menu
  ↓
Choose Operation
  ↓
Add / View / Search / Update / Delete / Statistics
  ↓
Save Changes if Required
  ↓
Return to Main Menu
  ↓
Exit
```

## Sample Records

The supplied JSON file contains 10 MCA student records:

- Jitesh Vishwakarma
- Prajwal Bhosale
- Vrushabh Sonawane
- Rishikesh Hedwe
- Param Gala
- Sneha Patil
- Sanika Patil
- Deeya Mathur
- Om Patil
- Ankit Sachin Kulkarni

## Note

The sample email addresses, phone numbers and marks are synthetic demonstration data and are not intended to represent real personal information.

## Author

- **Name:** Sakshi Ishwar Patil
- **Roll No.:** 150097926022
- **Course:** Masters of Computer Applications (MCA)
- **Subject:** Python Programming
- **Project Type:** Assignment - 1
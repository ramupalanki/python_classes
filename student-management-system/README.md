# Student Management System - Python OOP

## 1. Project Overview

This project is a small **Student Management System** built using Python Object-Oriented Programming (OOP).

It demonstrates the following core Python OOP concepts:

- Class
- Objects
- `__init__()` constructor
- Instance attributes
- Instance methods
- Class variable
- Class method
- Updating object data
- Calculating average marks

## 2. Requirements

Create a `Student` class with:

- Name
- Email
- Student ID
- Course
- Marks

The program creates multiple Student objects and provides methods to:

1. Display student details.
2. Update marks.
3. Calculate average marks.
4. Track the total number of students.
5. Retrieve the total number of students using a class method.

## 3. Project Structure

```text
student-management-system/
│
├── student_management.py
└── README.md
```

## 4. How to Run

### Step 1: Install Python

Install Python 3.x if it is not already installed.

Check the installation:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Step 2: Clone or download the repository

After checking the project into GitHub, clone it using:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### Step 3: Open the project directory

```bash
cd student-management-system
```

### Step 4: Run the program

```bash
python student_management.py
```

On systems where Python 3 is invoked as `python3`:

```bash
python3 student_management.py
```

## 5. Expected Output

The program displays details similar to:

```text
--------------------------------------------------
Name      : Ravi Kumar
Email     : ravi@example.com
Student ID: S001
Course    : Python
Marks     : [85, 90, 78]
Average   : 84.33
--------------------------------------------------
Name      : Priya Sharma
Email     : priya@example.com
Student ID: S002
Course    : Data Science
Marks     : [92, 88, 95]
Average   : 91.67
--------------------------------------------------
Name      : Arjun Reddy
Email     : arjun@example.com
Student ID: S003
Course    : Cloud Computing
Marks     : [76, 81, 84]
Average   : 80.33

After updating Ravi's marks:
--------------------------------------------------
Name      : Ravi Kumar
Email     : ravi@example.com
Student ID: S001
Course    : Python
Marks     : [90, 91, 88]
Average   : 89.67

Total number of students: 3
```

## 6. OOP Concepts Explained

### Class

`Student` is the class that acts as a blueprint for creating student objects.

```python
class Student:
```

### Objects

Three objects are created from the `Student` class:

```python
student1 = Student(...)
student2 = Student(...)
student3 = Student(...)
```

Each object contains its own student information.

### `__init__()` Constructor

The `__init__()` method runs automatically whenever a new Student object is created.

```python
def __init__(self, name, email, student_id, course, marks):
```

It initializes the object's attributes.

### Instance Attributes

These belong to individual Student objects:

```python
self.name
self.email
self.student_id
self.course
self.marks
```

For example, `student1.name` and `student2.name` can contain different values.

### Instance Methods

Instance methods operate on a particular object.

Examples:

```python
student1.display_details()
student1.update_marks([90, 91, 88])
student1.calculate_average()
```

These methods use `self` to access the current object's data.

### Class Variable

The following variable belongs to the class rather than to one particular object:

```python
total_students = 0
```

Every time a Student object is created, it is increased:

```python
Student.total_students += 1
```

Therefore, it keeps track of the total number of Student objects created.

### Class Method

The `get_total_students()` method is a class method:

```python
@classmethod
def get_total_students(cls):
    return cls.total_students
```

It uses `cls` to access class-level data.

It can be called without creating another object:

```python
Student.get_total_students()
```

## 7. Important Difference: `self` vs `cls`

| Keyword | Used With | Purpose |
|---|---|---|
| `self` | Instance methods | Refers to the current object |
| `cls` | Class methods | Refers to the class |

Example:

```python
def calculate_average(self):
    return sum(self.marks) / len(self.marks)
```

Here, `self` accesses the marks of one particular student.

```python
@classmethod
def get_total_students(cls):
    return cls.total_students
```

Here, `cls` accesses the class variable.

## 8. Assignment / Practice Tasks

After understanding the basic implementation, try these enhancements:

### Task 1 - Add Phone Number

Add a `phone_number` attribute to the Student class.

### Task 2 - Add Grade Calculation

Create an instance method:

```python
calculate_grade()
```

For example:

- 90 and above -> A
- 80 to 89 -> B
- 70 to 79 -> C
- 60 to 69 -> D
- Below 60 -> F

### Task 3 - Add Student Search

Create a class method or separate manager class that can search students by Student ID.

### Task 4 - Add Multiple Subjects

Change the marks structure so that marks can be stored against subject names.

Example:

```python
{
    "Python": 90,
    "SQL": 85,
    "Git": 95
}
```

### Task 5 - Delete Student

Add functionality to remove a student and correctly update the total student count.

### Task 6 - User Input

Modify the program so that student information is entered through the terminal instead of being hard-coded.

## 9. GitHub Check-in Instructions

From the project directory:

### Initialize Git

```bash
git init
```

### Add the files

```bash
git add .
```

### Commit the changes

```bash
git commit -m "Add Student Management System using Python OOP"
```

### Add your GitHub remote

Replace the URL with your repository URL:

```bash
git remote add origin <YOUR-GITHUB-REPOSITORY-URL>
```

### Push the code

For a new repository using the `main` branch:

```bash
git branch -M main
git push -u origin main
```

If your repository already has a remote configured:

```bash
git push
```

## 10. Learning Outcome

After completing this project, you should be able to understand and demonstrate:

- How to define a Python class.
- How to create objects from a class.
- How `__init__()` initializes object data.
- How instance attributes work.
- How instance methods work.
- How a class variable can maintain shared information.
- How `@classmethod` works.
- The difference between `self` and `cls`.
- How objects can modify their own data.

## 11. File

The main Python implementation is available in:

```text
student_management.py
```

All code lines contain explanatory comments to make the example suitable for learning and revision.

# Super30 Learning Platform

## Project Description

This project is a mini **Super30 Learning Platform** created in Python.

The project demonstrates the major Object-Oriented Programming concepts covered so far:

- Classes and objects
- Constructors
- Inheritance
- Instance methods
- Class variables
- Class methods
- Static methods
- Multiple objects
- Encapsulation through object attributes

The class hierarchy is:

```text
User
|
+---- Student
|
+---- Mentor
```

## Class Design

### 1. User

The `User` class is the parent/base class.

It contains:

- `name`
- `email`
- `user_id`

It also contains the class variable:

```python
total_users = 0
```

This variable keeps track of the total number of User, Student, and Mentor objects created.

### 2. Student

`Student` inherits from `User`.

Student-specific attributes:

- `course_name`
- `completed_assignments`

Student methods:

- `register_course()`
- `submit_assignment()`
- `display_student_info()`

### 3. Mentor

`Mentor` inherits from `User`.

Mentor-specific attributes:

- `expertise`
- `students_assigned`

Mentor methods:

- `assign_student()`
- `display_mentor_info()`

## OOP Concepts Demonstrated

### Class Variable

The following class variable counts all users:

```python
total_users = 0
```

Every time a `User`, `Student`, or `Mentor` object is created, the count is increased.

### Class Method

The following class method returns the total user count:

```python
@classmethod
def get_total_users(cls):
    return cls.total_users
```

It is called using:

```python
User.get_total_users()
```

### Static Method

The `is_valid_email()` method validates an email address.

It does not depend on object or class data, so it is implemented as a static method:

```python
@staticmethod
def is_valid_email(email):
    return isinstance(email, str) and "@" in email and "." in email.split("@")[-1]
```

It can be called using:

```python
User.is_valid_email("ravi@example.com")
```

### Inheritance

`Student` and `Mentor` inherit common properties and methods from `User`.

```python
class Student(User):
```

and

```python
class Mentor(User):
```

Both child classes use:

```python
super().__init__(name, email, user_id)
```

to call the parent constructor.

### Constructors

The `__init__()` methods initialize object data.

For example:

```python
def __init__(self, name, email, user_id):
```

### Instance Methods

Methods such as `register_course()`, `submit_assignment()`, and `assign_student()` operate on individual objects.

## Example Functionality

The project demonstrates:

1. Creating multiple students.
2. Creating a mentor.
3. Registering students for a course.
4. Submitting assignments.
5. Assigning students to a mentor.
6. Displaying student information.
7. Displaying mentor information.
8. Validating an email using a static method.
9. Counting total users using a class method.

## How to Run

Make sure Python 3 is installed.

Open a terminal in the project folder and run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Expected Output

The output will be similar to:

```text
Ravi registered for Python Programming.
Anita registered for Python Programming.
Ravi submitted: Variables and Data Types.
Ravi submitted: Functions.
Anita submitted: Variables and Data Types.
Ravi assigned to mentor Kiran.
Anita assigned to mentor Kiran.

--- Student 1 Information ---
User ID: S101
Name: Ravi
Email: ravi@example.com
Course: Python Programming
Completed Assignments: Variables and Data Types, Functions

--- Student 2 Information ---
User ID: S102
Name: Anita
Email: anita@example.com
Course: Python Programming
Completed Assignments: Variables and Data Types

--- Mentor Information ---
User ID: M101
Name: Kiran
Email: kiran@example.com
Expertise: Python and Automation
Students Assigned: 2

--- Email Validation ---
Ravi email valid: True
Invalid email valid: False

--- Platform Statistics ---
Total users: 3
```

## GitHub Check-in

Initialize Git:

```bash
git init
```

Add the files:

```bash
git add .
```

Commit the project:

```bash
git commit -m "Add Super30 Learning Platform OOP project"
```

Add your GitHub repository:

```bash
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
```

Push the code:

```bash
git branch -M main
git push -u origin main
```

## Project Structure

```text
super30-learning-platform/
|
+-- main.py
+-- README.md
```

## Learning Outcome

After completing this project, you should understand how a real-world application can be modeled using Python classes, inheritance, constructors, instance methods, class variables, class methods, and static methods.

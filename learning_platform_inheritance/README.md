# Python Learning Platform - Inheritance

## What this project demonstrates

This project builds a small learning platform using Python inheritance.

### Class hierarchy

```text
                User
              /  |  \
             /   |   \
        Student Mentor Admin
```

## Concepts demonstrated

1. Parent class
2. Child classes
3. Inheritance
4. `super()`
5. Common properties and methods
6. Role-specific functionality
7. Method overriding
8. Runtime polymorphism

## Files

- `user.py` - Parent `User` class
- `student.py` - `Student` child class
- `mentor.py` - `Mentor` child class
- `admin.py` - `Admin` child class
- `main.py` - Creates objects and demonstrates the concepts

## How inheritance works

`Student`, `Mentor`, and `Admin` inherit from `User`.

The parent class contains common information:

- `name`
- `email`

It also contains common methods:

- `show_profile()`
- `login()`

Each child class adds its own properties and functionality.

### Student

- Course
- `enroll_course()`

### Mentor

- Subject
- `conduct_session()`

### Admin

- Department
- `manage_platform()`

## Method overriding

The `User` class has:

```python
def show_profile(self):
    ...
```

Each child class defines its own `show_profile()` method.

For example:

```python
student.show_profile()
mentor.show_profile()
admin.show_profile()
```

The method name is the same, but the behavior is different depending on the object.

## Runtime polymorphism

The following demonstrates runtime polymorphism:

```python
users = [student, mentor, admin]

for user in users:
    user.show_profile()
```

Python determines at runtime which version of `show_profile()` should be executed.

## How to run

Open a terminal in this folder and run:

```bash
python main.py
```

## Expected output

```text
Ravi logged into the learning platform.
Anita logged into the learning platform.
Kiran logged into the learning platform.

Ravi enrolled in Python.
Anita is conducting a Python session.
Kiran is managing the Training department.

--- Student Profile ---
Name   : Ravi
Email  : ravi@example.com
Course : Python

--- Mentor Profile ---
Name    : Anita
Email   : anita@example.com
Subject : Python

--- Admin Profile ---
Name       : Kiran
Email      : kiran@example.com
Department : Training
```

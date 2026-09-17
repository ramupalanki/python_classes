# Python Employee Inheritance

## Objective

Create a base `Employee` class and a child `Developer` class to demonstrate:

- Parent class
- Child class
- Inheritance
- `super()`
- Object creation
- Accessing parent class functionality from a child class

## Class Structure

```text
Employee
   |
   +---- Developer
```

## Employee Class

The `Employee` class contains:

- Employee ID
- Name
- Salary
- Department
- `display_details()` method

## Developer Class

The `Developer` class inherits from `Employee` and adds:

- Programming language
- Experience
- `display_developer_details()` method

The Developer class calls the inherited `display_details()` method to demonstrate inheritance.

## How to Run

Make sure Python is installed, then run:

```bash
python employee.py
```

## Expected Concepts

This project demonstrates basic Object-Oriented Programming (OOP) inheritance in Python.

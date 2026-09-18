# Online Learning Platform - Python Inheritance

## What to Build

Build a simple online learning platform using Python inheritance.

The project uses this inheritance structure:

```text
Course
   |
PremiumCourse
```

## Concepts Covered

- Classes and objects
- Constructors (`__init__`)
- Instance attributes
- Instance methods
- Inheritance
- Method overriding
- `super()`
- Class variables
- Class methods
- Input validation
- Basic documentation using comments and docstrings

## Course Class

The `Course` class contains:

- `course_name`
- `instructor`
- `duration`
- `price`

### Methods

#### `show_course_details()`

Displays the course information.

#### `calculate_discount(discount_percentage)`

Calculates the discount amount based on the course price.

The method validates that the discount percentage is between 0 and 100.

#### `get_course_count()`

A class method that returns the total number of courses created.

The shared class variable `course_count` is increased every time a `Course` or `PremiumCourse` object is created.

## PremiumCourse Class

`PremiumCourse` inherits from `Course`.

In addition to the attributes provided by `Course`, it contains:

- `mentor_support`
- `live_sessions`

The `show_course_details()` method is overridden to display both the common course information and premium-specific features.

`super()` is used to reuse functionality from the parent class.

## Project Structure

```text
online_learning_platform/
│
├── course.py
└── README.md
```

## How to Run

Make sure Python 3 is installed.

Open a terminal in the project folder and run:

```bash
python course.py
```

## Expected Output

The program creates one regular course and one premium course.

It displays:

- Course details
- Discount amount
- Price after discount
- Premium features
- Total number of courses created

Example:

```text
===== Regular Course =====
Course Name: Python Programming
Instructor: Ramu
Duration: 8 Weeks
Price: ₹4999.00
10% Discount: ₹499.90
Price After Discount: ₹4499.10

===== Premium Course =====
Course Name: Artificial Intelligence
Instructor: Ramu
Duration: 12 Weeks
Price: ₹8999.00
Mentor Support: Available
Live Sessions: 2 sessions per week
15% Discount: ₹1349.85
Price After Discount: ₹7649.15

===== Course Count =====
Total Courses Created: 2
```

## GitHub Check-in

After extracting the ZIP file:

```bash
git init
git add .
git commit -m "Add online learning platform using inheritance"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```

Replace `<your-github-repository-url>` with your GitHub repository URL.

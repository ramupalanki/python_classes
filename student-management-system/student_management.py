# Student Management System using Python OOP
# This program demonstrates classes, objects, instance methods,
# class variables, and class methods.

class Student:
    # Class variable used to track the total number of Student objects.
    total_students = 0

    # Constructor method used to initialize a Student object.
    def __init__(self, name, email, student_id, course, marks):
        # Store the student's name as an instance attribute.
        self.name = name
        # Store the student's email as an instance attribute.
        self.email = email
        # Store the student's ID as an instance attribute.
        self.student_id = student_id
        # Store the student's course as an instance attribute.
        self.course = course
        # Store the student's marks as a list of numbers.
        self.marks = marks
        # Increase the class variable whenever a Student object is created.
        Student.total_students += 1

    # Instance method used to display all student details.
    def display_details(self):
        # Display a separator for readability.
        print("-" * 50)
        # Display the student's name.
        print(f"Name      : {self.name}")
        # Display the student's email.
        print(f"Email     : {self.email}")
        # Display the student's ID.
        print(f"Student ID: {self.student_id}")
        # Display the student's course.
        print(f"Course    : {self.course}")
        # Display the student's marks.
        print(f"Marks     : {self.marks}")
        # Display the student's average marks.
        print(f"Average   : {self.calculate_average():.2f}")

    # Instance method used to replace the student's marks.
    def update_marks(self, new_marks):
        # Validate that the supplied marks are provided as a list or tuple.
        if not isinstance(new_marks, (list, tuple)):
            # Raise an error when the marks are not a list or tuple.
            raise TypeError("new_marks must be a list or tuple.")
        # Convert the supplied marks into a list and update the object.
        self.marks = list(new_marks)

    # Instance method used to calculate the average of the student's marks.
    def calculate_average(self):
        # Return 0 when the student has no marks.
        if not self.marks:
            return 0
        # Return the arithmetic mean of all marks.
        return sum(self.marks) / len(self.marks)

    # Class method used to return the total number of students.
    @classmethod
    def get_total_students(cls):
        # Return the current value of the class variable.
        return cls.total_students


# Create the first Student object.
student1 = Student(
    "Ravi Kumar",
    "ravi@example.com",
    "S001",
    "Python",
    [85, 90, 78],
)

# Create the second Student object.
student2 = Student(
    "Priya Sharma",
    "priya@example.com",
    "S002",
    "Data Science",
    [92, 88, 95],
)

# Create the third Student object.
student3 = Student(
    "Arjun Reddy",
    "arjun@example.com",
    "S003",
    "Cloud Computing",
    [76, 81, 84],
)

# Display details of the first student.
student1.display_details()

# Display details of the second student.
student2.display_details()

# Display details of the third student.
student3.display_details()

# Update the first student's marks.
student1.update_marks([90, 91, 88])

# Display the first student's updated details.
print("\nAfter updating Ravi's marks:")
student1.display_details()

# Display the total number of students using the class method.
print("\nTotal number of students:", Student.get_total_students())

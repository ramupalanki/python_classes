"""
Super30 Learning Platform
A mini Python project demonstrating:
- Inheritance
- Constructors
- Instance methods
- Class variables
- Class methods
- Static methods
- Multiple objects
"""

class User:
    # Class variable shared by all User, Student, and Mentor objects.
    total_users = 0

    def __init__(self, name, email, user_id):
        # Initialize common user information.
        self.name = name
        self.email = email
        self.user_id = user_id

        # Increase the total user count whenever a new object is created.
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        # Class method returns the number of users created.
        return cls.total_users

    @staticmethod
    def is_valid_email(email):
        # Static method validates an email without using object/class data.
        return isinstance(email, str) and "@" in email and "." in email.split("@")[-1]

    def display_user_info(self):
        # Instance method displays common user information.
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


class Student(User):
    def __init__(self, name, email, user_id):
        # Call the parent constructor to initialize common user details.
        super().__init__(name, email, user_id)

        # Student-specific attributes.
        self.course_name = None
        self.completed_assignments = []

    def register_course(self, course_name):
        # Assign a course to the student.
        self.course_name = course_name
        print(f"{self.name} registered for {course_name}.")

    def submit_assignment(self, assignment_name):
        # Add a submitted assignment to the student's completed list.
        if assignment_name not in self.completed_assignments:
            self.completed_assignments.append(assignment_name)
            print(f"{self.name} submitted: {assignment_name}.")
        else:
            print(f"{assignment_name} was already submitted by {self.name}.")

    def display_student_info(self):
        # Display inherited user information first.
        self.display_user_info()

        # Display student-specific information.
        print(f"Course: {self.course_name or 'Not assigned'}")
        print(
            "Completed Assignments: "
            + (", ".join(self.completed_assignments)
               if self.completed_assignments else "None")
        )


class Mentor(User):
    def __init__(self, name, email, user_id, expertise):
        # Call the parent constructor for common user information.
        super().__init__(name, email, user_id)

        # Mentor-specific attributes.
        self.expertise = expertise
        self.students_assigned = 0

    def assign_student(self, student):
        # Assign one student to the mentor.
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be assigned to a mentor.")

        self.students_assigned += 1
        print(f"{student.name} assigned to mentor {self.name}.")

    def display_mentor_info(self):
        # Display inherited user information first.
        self.display_user_info()

        # Display mentor-specific information.
        print(f"Expertise: {self.expertise}")
        print(f"Students Assigned: {self.students_assigned}")


# -------------------- Example Usage --------------------

# Create multiple Student objects.
student1 = Student("Ravi", "ravi@example.com", "S101")
student2 = Student("Anita", "anita@example.com", "S102")

# Create a Mentor object.
mentor1 = Mentor("Kiran", "kiran@example.com", "M101", "Python and Automation")

# Register students for courses.
student1.register_course("Python Programming")
student2.register_course("Python Programming")

# Submit assignments.
student1.submit_assignment("Variables and Data Types")
student1.submit_assignment("Functions")
student2.submit_assignment("Variables and Data Types")

# Assign students to the mentor.
mentor1.assign_student(student1)
mentor1.assign_student(student2)

# Display student information.
print("\n--- Student 1 Information ---")
student1.display_student_info()

print("\n--- Student 2 Information ---")
student2.display_student_info()

# Display mentor information.
print("\n--- Mentor Information ---")
mentor1.display_mentor_info()

# Use the static method.
print("\n--- Email Validation ---")
print("Ravi email valid:", User.is_valid_email(student1.email))
print("Invalid email valid:", User.is_valid_email("invalid-email"))

# Use the class method to count all users.
print("\n--- Platform Statistics ---")
print("Total users:", User.get_total_users())

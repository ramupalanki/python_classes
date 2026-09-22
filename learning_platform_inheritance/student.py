from user import User


class Student(User):
    """
    Student inherits common properties and methods from User.
    """

    def __init__(self, name, email, course):
        # Call the parent constructor
        super().__init__(name, email)

        # Student-specific property
        self.course = course

    def enroll_course(self):
        # Student-specific functionality
        print(f"{self.name} enrolled in {self.course}.")

    def show_profile(self):
        # Method overriding:
        # Student provides its own implementation of show_profile()
        print("\n--- Student Profile ---")
        print(f"Name   : {self.name}")
        print(f"Email  : {self.email}")
        print(f"Course : {self.course}")

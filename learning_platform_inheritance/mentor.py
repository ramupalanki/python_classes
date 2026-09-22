from user import User


class Mentor(User):
    """
    Mentor inherits common properties and methods from User.
    """

    def __init__(self, name, email, subject):
        # Call the parent constructor
        super().__init__(name, email)

        # Mentor-specific property
        self.subject = subject

    def conduct_session(self):
        # Mentor-specific functionality
        print(f"{self.name} is conducting a {self.subject} session.")

    def show_profile(self):
        # Method overriding:
        # Mentor provides its own implementation of show_profile()
        print("\n--- Mentor Profile ---")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"Subject : {self.subject}")

from user import User


class Admin(User):
    """
    Admin inherits common properties and methods from User.
    """

    def __init__(self, name, email, department):
        # Call the parent constructor
        super().__init__(name, email)

        # Admin-specific property
        self.department = department

    def manage_platform(self):
        # Admin-specific functionality
        print(f"{self.name} is managing the {self.department} department.")

    def show_profile(self):
        # Method overriding:
        # Admin provides its own implementation of show_profile()
        print("\n--- Admin Profile ---")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Department : {self.department}")

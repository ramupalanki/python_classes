class User:
    """
    Parent class representing a common user in the learning platform.
    """

    def __init__(self, name, email):
        # Common properties shared by all users
        self.name = name
        self.email = email

    def show_profile(self):
        # Common method that can be overridden by child classes
        print(f"Name  : {self.name}")
        print(f"Email : {self.email}")

    def login(self):
        # Common functionality for every user
        print(f"{self.name} logged into the learning platform.")

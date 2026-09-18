class Course:
    """Represents a basic online learning course."""

    # Class variable used to count all Course and PremiumCourse objects.
    course_count = 0

    def __init__(self, course_name, instructor, duration, price):
        # Store the basic course information.
        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        # Increase the shared course count whenever a course is created.
        Course.course_count += 1

    def show_course_details(self):
        """Display the details of the course."""
        print(f"Course Name: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Duration: {self.duration}")
        print(f"Price: ₹{self.price:.2f}")

    def calculate_discount(self, discount_percentage):
        """Calculate the discount amount for the course."""
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate the discount amount based on the original price.
        discount_amount = self.price * discount_percentage / 100
        return discount_amount

    @classmethod
    def get_course_count(cls):
        """Return the total number of courses created."""
        return cls.course_count


class PremiumCourse(Course):
    """Represents a premium course with additional learning benefits."""

    def __init__(
        self,
        course_name,
        instructor,
        duration,
        price,
        mentor_support,
        live_sessions
    ):
        # Initialize the common attributes using the parent class constructor.
        super().__init__(course_name, instructor, duration, price)

        # Store premium-specific features.
        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_course_details(self):
        """Display basic and premium course details."""
        # Reuse the parent class method instead of duplicating common details.
        super().show_course_details()
        print(f"Mentor Support: {self.mentor_support}")
        print(f"Live Sessions: {self.live_sessions}")


if __name__ == "__main__":
    # Create a regular course.
    python_course = Course(
        "Python Programming",
        "Ramu",
        "8 Weeks",
        4999
    )

    # Create a premium course using inheritance.
    ai_course = PremiumCourse(
        "Artificial Intelligence",
        "Ramu",
        "12 Weeks",
        8999,
        "Available",
        "2 sessions per week"
    )

    print("===== Regular Course =====")
    python_course.show_course_details()

    discount = python_course.calculate_discount(10)
    print(f"10% Discount: ₹{discount:.2f}")
    print(f"Price After Discount: ₹{python_course.price - discount:.2f}")

    print("\n===== Premium Course =====")
    ai_course.show_course_details()

    discount = ai_course.calculate_discount(15)
    print(f"15% Discount: ₹{discount:.2f}")
    print(f"Price After Discount: ₹{ai_course.price - discount:.2f}")

    print("\n===== Course Count =====")
    print(f"Total Courses Created: {Course.get_course_count()}")

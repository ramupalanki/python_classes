from student import Student
from mentor import Mentor
from admin import Admin


# Create objects of the child classes
student = Student("Ravi", "ravi@example.com", "Python")
mentor = Mentor("Anita", "anita@example.com", "Python")
admin = Admin("Kiran", "kiran@example.com", "Training")


# ---------------------------------------------------------
# 1. Inheritance
# ---------------------------------------------------------
# Student, Mentor, and Admin inherit login() from User.
student.login()
mentor.login()
admin.login()


# ---------------------------------------------------------
# 2. Role-specific functionality
# ---------------------------------------------------------
student.enroll_course()
mentor.conduct_session()
admin.manage_platform()


# ---------------------------------------------------------
# 3. Method overriding
# ---------------------------------------------------------
# All three objects use the same method name: show_profile().
# But each child class provides its own implementation.
student.show_profile()
mentor.show_profile()
admin.show_profile()


# ---------------------------------------------------------
# 4. Runtime polymorphism
# ---------------------------------------------------------
# The same show_profile() call works with different objects.
# Python decides which overridden method to execute at runtime.

print("\n--- Runtime Polymorphism ---")

users = [student, mentor, admin]

for user in users:
    user.show_profile()

"""
Employee Management System
--------------------------------
This project demonstrates basic Object-Oriented Programming (OOP)
concepts in Python using an Employee class.

OOP concepts demonstrated:
1. Class and Objects
2. Constructor (__init__)
3. Instance attributes
4. Instance methods
5. Updating object data
6. Calculating values from object data
"""


class Employee:
    """Represents an employee in the organization."""

    def __init__(self, employee_id, name, department, salary, designation):
        # Store employee details as instance attributes.
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

    def display_employee_info(self):
        """Display all information about the employee."""
        print("-" * 50)
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ₹{self.salary:,.2f}")
        print(f"Designation : {self.designation}")

    def update_salary(self, new_salary):
        """Update the employee's monthly salary."""
        self.salary = new_salary
        print(f"{self.name}'s salary updated to ₹{self.salary:,.2f}")

    def calculate_annual_salary(self):
        """Return the employee's annual salary."""
        return self.salary * 12


# ---------------------------------------------------------
# Create at least 5 Employee objects.
# ---------------------------------------------------------

employee1 = Employee(
    101, "Ravi Kumar", "QA", 75000, "QA Engineer"
)

employee2 = Employee(
    102, "Priya Sharma", "Development", 90000, "Senior Developer"
)

employee3 = Employee(
    103, "Arjun Reddy", "DevOps", 85000, "DevOps Engineer"
)

employee4 = Employee(
    104, "Sneha Rao", "HR", 65000, "HR Manager"
)

employee5 = Employee(
    105, "Vikram Singh", "Finance", 70000, "Financial Analyst"
)


# Store all employee objects in a list so that we can
# process them easily using a loop.
employees = [
    employee1,
    employee2,
    employee3,
    employee4,
    employee5
]


# ---------------------------------------------------------
# Display employee information and annual salary.
# ---------------------------------------------------------
for employee in employees:
    employee.display_employee_info()

    # Calculate annual salary using the class method.
    annual_salary = employee.calculate_annual_salary()
    print(f"Annual Salary: ₹{annual_salary:,.2f}")


# ---------------------------------------------------------
# Demonstrate updating an employee's salary.
# ---------------------------------------------------------

print("\nSALARY UPDATE")
print("=" * 50)

# Update Ravi's monthly salary.
employee1.update_salary(80000)

# Display the updated information.
employee1.display_employee_info()


# ---------------------------------------------------------
# Final employee summary.
# ---------------------------------------------------------

print("\nFINAL EMPLOYEE SUMMARY")

for employee in employees:
    print(
        f"{employee.employee_id} - "
        f"{employee.name} - "
        f"{employee.designation} - "
        f"Annual Salary: ₹{employee.calculate_annual_salary():,.2f}"
    )

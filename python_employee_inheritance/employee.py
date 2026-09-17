class Employee:
    # Constructor for the parent class
    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    # Method available to all Employee objects
    def display_details(self):
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("Department  :", self.department)


class Developer(Employee):
    # Constructor for the child class
    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language,
        experience
    ):
        # Call the parent class constructor
        super().__init__(employee_id, name, salary, department)

        # Additional attributes specific to Developer
        self.programming_language = programming_language
        self.experience = experience

    # Additional method specific to Developer
    def display_developer_details(self):
        # Calling the inherited parent class method
        self.display_details()

        # Display Developer-specific details
        print("Programming Language :", self.programming_language)
        print("Experience           :", self.experience, "years")


# Create Employee object
employee1 = Employee(
    101,
    "Ravi",
    50000,
    "HR"
)

# Create Developer objects
developer1 = Developer(
    102,
    "Anil",
    80000,
    "IT",
    "Python",
    5
)

developer2 = Developer(
    103,
    "Priya",
    90000,
    "IT",
    "Java",
    7
)

# Display Employee details
print("----- Employee Details -----")
employee1.display_details()

# Display Developer details
print("\n----- Developer 1 Details -----")
developer1.display_developer_details()

# Demonstrate that Developer can directly access inherited functionality
print("\n----- Developer 2 Details -----")
developer2.display_developer_details()

print("\n----- Inherited Method Demonstration -----")
developer1.display_details()

# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an 
# Employee object that exists independently of it.
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def get_details(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: List to store references to Employee objects
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        return f"{self.name} Department Employees:\n" + "\n".join(emp.get_details() for emp in self.employees)

# Example usage
if __name__ == "__main__":
    # Create Employee objects independently
    emp1 = Employee("Alice Smith", 1001)
    emp2 = Employee("Bob Johnson", 1002)
    
    # Create Department and add existing Employee objects
    dept = Department("Engineering")
    dept.add_employee(emp1)
    dept.add_employee(emp2)
    
    print(dept.list_employees())
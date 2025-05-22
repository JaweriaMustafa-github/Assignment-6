#Create a class Employee with:
# >a public variable name,
# >a protected variable _salary, and
# >a private variable __ssn.
# >Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self , name , salary , ssn):
        self.name = name #Public
        self._salary = salary #Protected 
        self.__ssn = ssn #Private


emp = Employee("John", 10000 , "123-45-6789")

print("\n# Accessing public variable #")
print(f"Name (public): ", emp.name)

print("\n")
print("# Accessing protected variable (allowed but not recommended) #")
print(f"Salary (_protected): ", emp._salary)

print("\n")
print("# Accessing private variable directly (will cause AttributeError) #")
try:
    print(f"SSN (__private): ", emp.__ssn)
except AttributeError as e:
    print("Cannot access __ssn directly:", e)

#Accessing private variable using name mangling
print("Accessing private (__ssn) using name mangling:", emp._Employee__ssn)
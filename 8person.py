# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and 
# use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name , subject):
        super().__init__(name) # Call base class constructor
        self.subject = subject

t1 = Teacher("Mr Alice", "History")

# Access attributes
print("Name: ", t1.name)
print("Subject: ", t1.subject)
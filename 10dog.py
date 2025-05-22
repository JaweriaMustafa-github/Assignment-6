# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including
# the dog's name.

class Dog :
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: WOOF! WOOF!")
        
# Creating an object of dog
my_dog = Dog("Partner", "Cyberian Husky")

# Accessing instance variables and method
print("Dog's name:", my_dog.name)
print("Dog's breed:", my_dog.breed)
my_dog.bark()
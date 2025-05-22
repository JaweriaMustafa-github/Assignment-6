# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be 
# used.

class MathUtils:

    @staticmethod
    def add(a,b):
        return a + b
    
# Using the static method without creating an instance
result = MathUtils.add(6,4)
print(f"Sum:", result)
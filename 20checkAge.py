# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. 
# Handle it with try...except.

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return f"Age {age} is valid"

# Example usage
if __name__ == "__main__":
    try:
        print(check_age(20))  # Valid age
        print(check_age(15))  # Will raise InvalidAgeError
    except InvalidAgeError as e:
        print(f"Error: {e}")
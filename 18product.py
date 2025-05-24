# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and 
# @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

# Example usage
if __name__ == "__main__":
    product = Product("Laptop", 1000)
    print(product.price)  # Output: 1000
    product.price = 1200  # Update price
    print(product.price)  # Output: 1200
    del product.price     # Delete price attribute
    # Accessing price after deletion will raise AttributeError
    try:
        print(product.price)
    except AttributeError as e:
        print(f"Error: {e}")
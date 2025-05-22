# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from 
# outside the class.

class Car:
    #Public variable
    brand = "Honda"

    #Public method
    def start(self):
        print(f"{self.brand} Civic has started.")

my_car = Car()

#access the public variable
print(f"Car brand: {my_car.brand}")

#access the public method
my_car.start()
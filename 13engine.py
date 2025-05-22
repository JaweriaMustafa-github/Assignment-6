# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.

class Engine:
    def __init__ (self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} horsepower is not running."

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine # Composition: Engine object is part of Car

    def start_car(self):
        return f"{self.make} {self.model} : {self.engine.start()}"

#Example 
if __name__ == "__main__":
    engine = Engine(200)
    car = Car("Toyota" , "Corolla" , engine)
    print(car.start_car())
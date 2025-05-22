# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temperature_Converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
# Example usage:
print("0 degree Celsius to ", Temperature_Converter.celsius_to_fahrenheit(0) , "Fahrenheit")    
print("100 degree Celsius to ", Temperature_Converter.celsius_to_fahrenheit(100) , "Fahrenheit")  
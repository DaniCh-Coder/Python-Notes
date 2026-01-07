# Temprature conversion from Celsius to Fahrenheit and vice versa
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# Example usage
if __name__ == "__main__":
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is equal to {temp_f}°F.")
    
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is equal to {temp_c}°C.")

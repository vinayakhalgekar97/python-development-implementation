# Write a Python program to convert Celsius to Fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (1.8 * celsius) + 32

try:
    celsius_value = float(input("Enter value in celsius: "))
    result = convert_celsius_to_fahrenheit(celsius_value)
except TypeError as e:
    print(f"ERROR: {e}")
else:
    print(f"{celsius_value} degree celsius = {result} F")
finally:
    pass
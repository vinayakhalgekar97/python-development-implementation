# Write a Python program to convert kilometers to miles.
def km_to_miles(kilometre):
    return kilometre * 0.62137

try:
    km_value = float(input("Enter the value in Kilometer: "))
    result = km_to_miles(km_value)
except TypeError as e:
    print(f"ERROR: {e}")
else:
    print(f"{km_value} KM = {result} miles")
finally:
    print("OPERATION ENDED...")
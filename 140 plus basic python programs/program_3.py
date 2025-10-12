# Write a Python program to find the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

try:
    base = int(input("Enter base unit of the triangle: "))
    height = int(input("Enter height unit of the triangle: "))
    
    result = triangle_area(base=base, height=height)
except TypeError as e:
    print(f"ERROR: {e}")
else:
    print(f"The area of the triangle is {result}")
finally:
    print("PROGRAM ENDED...")
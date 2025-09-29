"""List Comprehension in Python"""

"""Syntax: [expression for item in iterable if condition]
Parameters:
    expression: operation or value to include in the new list.
    item: current element from the iterable.
    iterable: sequence like a list, tuple or range.
    if condition (optional): filter to include only items that satisfy the condition."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print(even_numbers)
print(odd_numbers)
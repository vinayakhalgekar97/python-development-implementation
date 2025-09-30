"""Python Sets"""
"""Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.
* Can store None values.
* Implemented using hash tables internally.
* Do not implement interfaces like Serializable or Cloneable.
* Python sets are not inherently thread-safe; synchronization is needed if used across threads."""

"""Creating a Set in Python"""
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numbers)

even_numbers = set([2, 4, 6, 8, 10, 12])
print(even_numbers)

"Sets do not support indexing. Trying to access an element by index (set[0]) raises a TypeError."

"""Adding Elements to a Set in Python"""
numbers.add(11)
print(numbers)

numbers.update([12, 13, 14])
print(numbers)

numbers.update([15])
print(numbers)

"""Accessing a Set in Python"""
"""We can loop through a set to access set items as set is unindexed and do not support accessing elements by indexing. Also we can use in keyword which is membership operator to check if an item exists in a set."""
# for number in numbers:
#     print(number, end=" ")

"""Removing Elements from the Set in Python"""
# Using remove() Method or discard() Method
numbers.remove(15)
print(numbers)

numbers.discard(14)
print(numbers)

# Using pop() Method
numbers.pop()
print(numbers)

# Using clear() Method
numbers.clear()
print(numbers)
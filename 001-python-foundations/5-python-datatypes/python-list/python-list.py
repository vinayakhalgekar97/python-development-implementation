"""Python Lists: a list is a built-in data structure that can hold an ordered collection of items.
Can contain duplicate items
Mutable: items can be modified, replaced, or removed
Ordered: maintains the order in which items are added
Index-based: items are accessed using their position (starting from 0)
Can store mixed data types (integers, strings, booleans, even other lists)"""

# Creating a List
# 1. Using Square Brackets
fruits = ["Apple", "Banana", "Cherry", "Watermelon", "Pomegranate"]
print(fruits)

# 2. Using list() Constructor
even_numbers = list([2, 4, 6, 8, 10, 12])
odd_numbers = list((1, 3, 5, 7, 9, 11))
list_names = list("Vinayak Halgekar")
print(even_numbers)
print(odd_numbers)
print(list_names)

# Accessing List Elements
print(fruits[0])
print(fruits[1])
print(fruits[-1])

print(fruits[1:4])

# Adding Elements into List
# 1. append(): Adds an element at the end of the list.
fruits.append("Orange")
fruits.append("Papaya")
print(fruits)

# 2. extend(): Adds multiple elements to the end of the list.
fruits.extend(["Coconut", "Mango", "Kiwi"])
print(fruits)

# 3. insert(): Adds an element at a specific position.
fruits.insert(1, "Pear")
print(fruits)
fruits.insert(3, "Guava")
print(fruits)

# 4. clear(): removes all items.
# fruits.clear()
# print(fruits)

# Updating Elements into List
fruits[2] = "Grapes"
print(fruits)

# Removing Elements from List
# 1. remove(): Removes the first occurrence of an element.
fruits.remove("Guava")
print(fruits)

# 2. pop(): Removes the element at a specific index or the last element if no index is specified.
fruits.pop(2)
print(fruits)

fruits.pop(-1)
print(fruits)

fruits.pop()
print(fruits)

# 3. del statement: Deletes an element at a specified index.
del fruits[1]
print(fruits)

del fruits[-1]
print(fruits)

# Iterating Over Lists
for fruit in fruits:
    print(fruit)

# Nested Lists 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
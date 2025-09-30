# Python Loops – The Basics
"""In Python, there are two main kinds of loops:"""
"""for loop → Iterates over a sequence (list, string, tuple, range, etc.)."""
# for number in [1,2,3]:
#     print(number)
    
"""while loop → Repeats as long as a condition is True."""
# i = 0
# while i <= 5:
#     print(i)
#     i += 1

"""Nested Loops
A nested loop is a loop inside another loop.
👉 For each iteration of the outer loop, the inner loop runs completely."""
# column_no = 5
# for row in range(0, column_no):
#     for column in range(0, column_no):
#         print(f"{row, column}", end=" ")
#     print()


"""
* 
* *
* * *
* * * *
* * * * *
"""
# for row in range(0, 5):
#     for column in range(0, row+1):
#         print("*", end=" ")
#     print("")

"""
* * * * *
* * * *
* * *
* *
*
"""
# for row in range(5, -1, -1):
#     for column in range(0, row+1):
#         print("*", end=" ")
#     print()

"""Multiplication Table of a particular number"""
# row = int(input("Multiplication Table: "))
# for column in range(1, 11):
#     print(f"{row}x{column}={row*column}")

"""
    *
   **
  ***
 ****
*****
"""
# column = 5
# for rows in range(1, column+1):
#     for empty_column in range(1, (column+1)-rows):
#         print(" ", end="")
#     for star_column in range(rows):
#         print("*", end="")
#     print()

"""
    *
   * *
  * * *
 * * * *
* * * * * 
"""
column = 5
for rows in range(1, column+1):
    for empty_column in range(1, (column+1)-rows):
        print(" ", end="")
    for star_column in range(rows):
        print("*", end=" ")
    print()

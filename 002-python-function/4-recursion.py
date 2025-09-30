"""
Recursion in Python: Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.

Working of Recursion: A recursive function is just like any other Python function except that it calls itself in its body. Let's see basic structure of recursive function:
    def recursive_function(parameters):
        if base_case_condition:
            return base_result
        else:
            return recursive_function(modified_parameters)

Recursive function contains two key parts:
Base Case: The stopping condition that prevents infinite recursion.
Recursive Case: The part of the function where it calls itself with modified parameters.
"""

"""Example 1: Factorial Calculation"""
def factorial(n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
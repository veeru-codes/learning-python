# debugging with pdb
# - pdb is the built-in Python debugger that allows you to set breakpoints, step through code, and inspect variables at runtime.
# - you can use pdb to find and fix bugs in your code by allowing you to interact with your code as it runs.
# - to use pdb, you can import it and set a breakpoint using pdb.set_trace() at the point where you want to start debugging.
# - once you hit the breakpoint, you can use various commands to step through your code, inspect variables, and evaluate expressions.
# - some common pdb commands include:
#   - l (list): show the current line of code and surrounding lines
#   - n (next): execute the next line of code
#   - s (step): step into a function call
#   - c (continue): continue execution until the next breakpoint
#   - p (print): print the value of a variable or expression

import pdb

# first = "John"
# second = "Doe"
# result = first + " " + second
# pdb.set_trace()  # Set a breakpoint here
# third = "Smith"
# final_result = result + " " + third
# print(final_result)

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = 3.14 * radius ** 2
    return area

pdb.set_trace()  # Set a breakpoint here
area = calculate_area(-5)
print(area)
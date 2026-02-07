# built-in modules
# - built-in modules are modules that are included with the Python standard library, and you can import and use them in your code without installing anything
# - some examples of built-in modules are: math, random, datetime, os, sys

# random module
# - the random module provides functions for generating random numbers and performing random operations
import random

# you can also import the module with an alias
# - import random as rnd

# imports all functions from the random module (not recommended)
# - from random import *  

# you can also import specific functions from the module
# - from random import random, randint, choice, shuffle  

print(random.random())  # generates a random float between 0 and 1
print(random.randint(1, 10))  # generates a random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # randomly selects an item from a list

# shuffle modifies the list in place and returns None
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  # shuffles the list in place
print(my_list)  # now print the shuffled list
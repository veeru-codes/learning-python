import math

# def performOperation(n1, n2, operation="sum"):
#     if operation == "sum":
#         return n1 + n2
#     if operation == "product":
#         return n1 * n2


# sum = performOperation(20, 2, operation="sum")
# product = performOperation(30, 40, operation="product")

# print(sum, product)


# We can capture multiple arguments with the help of '*args'
# Keyword arguments (**kwargs) must come after positional arguments (*args)
# Afterwards, keyword arguments can be in any order


def performOperation(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    if operation == "product":
        return math.prod(args)


sum = performOperation(1, 2, 3, operation="sum")
product = performOperation(1, 2, 3, operation="product")

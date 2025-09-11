# nested lists
nested_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
]

# accessing values
print(nested_lists[0][0])

# looping
for nested_list in nested_lists:
    for char in nested_list:
        print(char)

# nested list comprehension
chars = [char for nested_list in nested_lists for char in nested_list]
print(chars)

# creating a nested list with list comprehension
nums = [[j for j in range(0, 3)] for i in range(0, 3)]
print(nums)

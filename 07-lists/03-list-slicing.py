# slicing
# - make new lists using slices of the old list
# - some_list[start:end:step]

# - start --> what index to start slicing from
#         --> if you enter a negative number, it will slice that many from the end
first_list = [1, 2, 3, 4, 5]
print(first_list[1:]) # [2, 3, 4, 5]
print(first_list[3:]) # [4, 5]
print(first_list[-1:]) # [5]
print(first_list[-3:]) # [3, 4, 5]

# - end --> the index to copy up to (exclusive counting)
#       --> with negative numbers, how many items to exclude from the end
second_list = [4, 5, 6, 7, 8, 9, 10]
print(second_list[:2]) # [4, 5]
print(second_list[:4]) # [4, 5, 6, 7]
print(second_list[1:3]) # [5, 6]
print(second_list[:-2]) # [4, 5, 6, 7, 8]
print(second_list[2:-2]) # [6, 7, 8]

# - step --> it's basically the number to count at a time
#        --> with negative numbers, reverse the order
third_list = [7, 8, 9, 10, 11, 12]
print(third_list[1::2]) # [8, 10, 12]
print(third_list[::2]) # [7, 9, 11]
print(third_list[1::-1]) # [8, 7]
print(third_list[::-2]) # [12, 10, 8]
print(third_list[2::-2]) # [9, 7]

# tricks
# reversing lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_numbers = numbers[::-1]

string = 'this is a string'
reversed_string = string[::-1]

# modifying lists
numbers[1:3] = [10, 11, 12] # [1, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10]

# swapping values
names = ["james", 'michael']
names[0], names[1] = names[1], names[0]

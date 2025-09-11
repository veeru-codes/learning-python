# the syntax
# - [___ for ___ in ___]
# - []

numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * num for num in numbers]

# doubled_numbers = []
# for num in numbers:
#     doubled_numbers.append(num * num)

name = 'colt'
capital_chars = [char.upper() for char in name]

# capital_chars = []
# for char in name:
#     capital_chars.append(char.upper())

nums = [num * 10 for num in range(1, 6)]
string_list = [str(num) for num in nums]

# list comprehension with conditional logic
# using if
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in nums if num % 2 == 0]

# using if...else...
random = [num * 2 if num % 2 == 0 else num / 2 for num in nums]

# using in
with_vowels = "this is so much fun!"
consonants = ''.join(char for char in with_vowels if char not in 'aeiou')
print(consonants)

# all
# return true if all elements of the iterable are truthy (or if the iterable is empty)
people = ['charlie', 'casey', 'cody', 'carly', 'cristina']
print(all([name[0] == 'c' for name in people]))

nums = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in nums))

# any
# return true if any element of the iterable is truthy.
# if the iterable is empty, returns false
nums = [1, 2, 3, 4, 5]
print(any(n % 2 == 0 for n in nums))

# sorted
# returns a new sorted list from the items in iterable
numbers = [1, 2, 3, 4, 5]
# numbers.sort()   -- sorts in-place
print(sorted(numbers))
print(sorted(numbers, reverse=True))

users = [
    {'name': 'samuel', 'age': 25},
    {'name': 'katie', 'age': 30},
    {'name': 'jeff', 'age': 52},
    {'name': 'carly', 'age': 16},
    {'name': 'cody', 'age': 4},
]

print(sorted(users, key=len))  # sorted based on the length of each dictionary

print(sorted(users, key=lambda user: user['name']))
# [{'name': 'carly', 'age': 16}, {'name': 'cody', 'age': 4}, {'name': 'jeff', 'age': 52}, {'name': 'katie', 'age': 30}, {'name': 'samuel', 'age': 25}]

print(sorted(users, key=lambda user: user['age']))
# [{'name': 'cody', 'age': 4}, {'name': 'carly', 'age': 16}, {'name': 'samuel', 'age': 25}, {'name': 'katie', 'age': 30}, {'name': 'jeff', 'age': 52}]

print(sorted(users, key=lambda user: user['age'], reverse=True))
# [{'name': 'jeff', 'age': 52}, {'name': 'katie', 'age': 30}, {'name': 'samuel', 'age': 25}, {'name': 'carly', 'age': 16}, {'name': 'cody', 'age': 4}]

# max
# - returns the largest item in an iterable or the largest of two or more arguments
names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(numbers))  # 5
print(max('hello world'))  # 'w'
print(max(names, key=lambda name: len(name)))  # Ollivander

# min
# - returns the smallest item in an iterable or the smallest of two or more arguments
print(min(numbers))  # 1
print(min('hello'))  # 'e'
print(min(names, key=lambda name: len(name)))  # Tim

# reversed
# returns an iterator
print(reversed(numbers))  # <list_reverseiterator object at 0x105993f10>

# abs
# return the absolute value os a number
# the argument may be an integer or a floating point number
print(abs(-5))  # 5

# sum
# takes an iterable and an iterable start
# return the sum of start and the items of an iterable from left to right abd returns th total
# start defaults to 0
print(sum(numbers))  # 15
print(sum(numbers), 10)  # 25
print(sum((1.5, 2, 3, 6)))  # 12.5

# round
# return number rounded to ndigits precision after the decimal point.
# if ndigits is omitted or is None, it returns the nearest integer to its input
print(round(10.2))  # 10.2
print(round(3.51234, 3))  # 3.512
print(round(3.51234, None))  # 4


def sum_floats(*args):
    return sum([arg for arg in args if type(arg) == float])


print(sum_floats(1.5, 2.4, 'awesome', [], 1))

# zip
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

print(list(zip(nums1, nums2)))  # [(1, 4), (2, 5), (3, 6)]
print(dict(zip(nums1, nums2)))  # {1: 4, 2: 5, 3: 6}

nums3 = [10, 20, 30, 40, 50]
print(list(zip(nums3, nums2)))  # [(10, 4), (20, 5), (30, 6)]

words = ['hi', 'lol', 'haha', ':)']
print(list(zip(words, nums1, nums2)))  # [('hi', 1, 4), ('lol', 2, 5), ('haha', 3, 6)]

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}  # {'dan': 98, 'ang': 91, 'kate': 78}

print(final_grades)

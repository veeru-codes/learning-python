# the syntax
# -- { ___:___ for ___ in ___ }

numbers = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
squared = {key: value * value for key, value in numbers.items()}

squares = {num: num * num for num in [1, 2, 3, 4, 5]}
print(squares)

# conditional logic with dictionaries
num_list = [1, 2, 3, 4, 5]
num_even = {num: ('even' if num % 2 == 0 else 'odd') for num in num_list}
print(num_even)

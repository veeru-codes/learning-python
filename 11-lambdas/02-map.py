# a standard function that accepts at least two arguments, a function and an "iterable"
# iterable -- something that can be iterated over (lists, strings, dictionaries, sets, tuples)
# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

nums = [1, 2, 3, 4, 5]

doubles = list(map(lambda x: x * 2, nums))
print(doubles)

names = ['veera', 'thaseen', 'pranava', 'pari']
capitalized_names = list(map(lambda x: x.capitalize(), names))
print(capitalized_names)

names_dict = [
    {'first': 'veera', 'last': 'pottipati'},
    {'first': 'thaseen', 'last': 'avm'},
    {'first': 'pranava', 'last': 'pottipati'},
    {'first': 'pari', 'last': 'yadati'},
]

last_names = list(map(lambda x: x['last'], names_dict))
print(last_names)

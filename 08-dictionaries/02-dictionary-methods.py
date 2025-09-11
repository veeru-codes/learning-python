# get     - retrieves a key in an object and return None instead of KeyError if the key does not exist
# pop     - takes a single argument corresponding to a key and removes that key-value pair from the dictionary
#         - returns the value corresponding to the key that was removed
# popitem - removes a random key in a dictionary
# clear   - clears all the keys and values in a dictionary
# copy    - makes a copy of a dictionary
# fromkeys - creates key-value pairs from comma separated values
# update  - update keys and values in a dictionary with another set of key value pairs

instructor = {
    'name': 'colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'python',
    'is_hilarious': True,
    44: 'my favorite number'
}

# get
print(instructor.get('name'))  # 'colt'
print(instructor.get('favorite_language'))  # 'python'
print(instructor.get('phone_number'))  # None

# pop and popitem
print(instructor.pop(44))
print(instructor.popitem())

# clear
user = dict(name="john doe", age=22, gender='male')
user.clear()
print(user)

# copy
user = {"name": "john doe", "age": 22, "gender": "male"}
user_clone = user.copy()
print(user == user_clone)
print(user is user_clone)

# fromkeys
dict1 = {}.fromkeys('a', 'b')  # {'a': 'b'}

dict2 = {}.fromkeys(['key1', 'key2', 'key3'], 'value')
# dict2 = {
#   'key1': 'value',
#   'key2': 'value',
#   'key3': 'value'
# }

dict3 = {}.fromkeys('key', ['value1', 'value2', 'value3'])
# dict3 = {
#   'k': ['value1', 'value2', 'value3'],
#   'e': ['value1', 'value2', 'value3'],
#   'y': ['value1', 'value2', 'value3']
# }

# update
first = {'a': 1, 'b': 2, 'c': 3}
second = {}
second.update(first)

first['c'] = 4

print(first, second)

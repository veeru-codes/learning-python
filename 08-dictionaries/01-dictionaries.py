# a data structure that consists of key value pairs
# we use the keys to describe our data and the values to represent the data
# keys and values are separated by a colon
# keys are almost always numbers or strings

# -----------------------------------------------------------------------------------------------------
# since Python version 3.7, insertion order is officially guaranteed
# for standard Python dictionaries (i.e., for standard Python dict objects).
# -- keys stay in the order you add them.
# -- iterating over .keys(), .values(), or .items() follows that same order.
# -- deleting a key leaves the remaining keys' order intact. adding a new key appends it to the end.
# -----------------------------------------------------------------------------------------------------

instructor = {
    'name': 'colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'python',
    'is_hilarious': True,
    44: 'my favorite number'
}

# another approach is to use the dict function.
# you assign values to keys by passing in keys and values separated by an =

user = dict(name="john doe", age=22, gender='male')

# accessing data
favorite_number = instructor[44]
name = user['name']
age = user['age']
gender = user['gender']

# iterating dictionaries
# -- accessing keys
for key in user.keys():
    print(key, user[key])

# -- accessing values
for value in user.values():
    print(value)

# -- accessing items
for key, value in user.items():
    print(f"{key}: {value}")

# test for the existence of a key or value
print("name" in instructor)
print("phone" in instructor)
print(4 in instructor.values())

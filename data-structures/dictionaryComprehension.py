animals = [("a", "aardvark"), ("b", "bear"), ("c", "cat"), ("d", "dog")]

animalsDict1 = {item[0]: item[1] for item in animals}
print(animalsDict1)

# More elegant way using tuples

# Here each item in the 'animals' list is a tuple
# we are unpacking them -- key, value = ('a', 'aardvark')

animalsDict2 = {key: value for (key, value) in animals}
print(animalsDict2)

print(list(animalsDict2.items()))

users = [
    {
        "name": "John",
        "age": 17,
        "hobbies": ["reading books", "listening music"],
    },
    {
        "name": "Veerendra",
        "age": 24,
        "hobbies": ["reading books", "cooking"],
    },
    {
        "name": "Thaseen",
        "age": 22,
        "hobbies": ["listening music", "cooking"],
    },
]

eligibleUsers = [user for user in users if user["age"] >= 18]
print(eligibleUsers)

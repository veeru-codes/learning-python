# __repr__
# - __repr__ is a special method in Python that is used to define the string representation of an object.
# - It is called by the built-in repr() function and is also used when you print an object or when you inspect it in the interactive shell.
# - The purpose of __repr__ is to provide a string that would be a valid Python expression that can be used to recreate the object,
# - or at least give a detailed representation of the object for debugging purposes.

class User:
    user_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.user_count += 1

    # !r is used to get the string representation of the object for debugging purposes
    def __repr__(self):
        return f'User(name={self.name!r}, age={self.age!r})'


# creating an instance of the User class
user1 = User('Alice', 30)

# printing the user object will call the __repr__ method
print(user1)  # Output: User(name='Alice', age=30)

# class method
# - a method that is bound to the class and not the instance of the class.
# - it can modify a class state that applies across all instances of the class.

class User:
    user_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    # class method to create an instance of the User class from a string
    # - this is a common use case for class methods,
    # - where you want to provide an alternative constructor for the class
    # - that can create an instance from a different format of data (e.g., a string, a dictionary, etc.)
    @classmethod
    def from_string(cls, user_string):
        name, age = user_string.split(',')
        return cls(name, int(age))


# creating instances of the User class
user1 = User('Alice', 30)
user2 = User('Bob', 25)

# calling the class method to get the total number of users created
print(User.get_user_count())  # Output: 2

# creating an instance of the User class using the from_string class method
user3 = User.from_string('Charlie,35')
user3.display_info()  # Output: Name: Charlie, Age: 35
print(User.get_user_count())  # Output: 3

# class:
# - a blueprint for creating objects (a particular data structure),
# - providing initial values for state (member variables or attributes),
# - and implementations of behavior (member functions or methods).

class User:
    # class variable (shared by all instances of the class)
    user_count = 0

    # constructor method
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age  # instance variable
        User.user_count += 1  # increment the class variable each time a new instance is created

    # method to display user information
    # each method in a class must have self as the first parameter, which refers to the instance of the class
    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def is_adult(self):
        return self.age >= 18

    def have_birthday(self):
        self.age += 1


# creating an instance of the User class
user1 = User('Alice', 30)
user2 = User('Bob', 25)

# calling the method to display user information
user1.display_info()  # Output: Name: Alice, Age: 30
user2.display_info()  # Output: Name: Bob, Age: 25

# total number of users created
print(User.user_count)  # Output: 2

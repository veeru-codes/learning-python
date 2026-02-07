# __name__
# - __name__ is a special variable in Python that represents the name of the current module
# - when a module is run directly, __name__ is set to "__main__"
# - when a module is imported, __name__ is set to the name of the module
# - this allows you to write code that can be run both as a script and as a module

from my_module import say_hi


def sai_hello():
    print(f"Hello from {__name__}")


if __name__ == "__main__":
    # this code will only run if the module is run directly, not if it is imported
    print("This code is running directly")
    say_hi()  # prints "Hi from my_module", because __name__ is set to "my_module" when the module is imported
    sai_hello()  # prints "Hello from __main__", because __name__ is set to "__main__" when the module is run directly

# handle errors with try-except
# - try: code that may raise an error
# - except: code that runs if an error occurs in the try block
# - you can have multiple except blocks to handle different types of errors
# - you can also have a generic except block to catch any error

def divide(a, b):
    try:
        return a / b
    except TypeError:
        print("both arguments must be numbers")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except Exception as e:
        print(f"an error occurred: {e}")

divide(10, 0) # cannot divide by zero
divide(10, "a") # both arguments must be numbers

def get_key(d, key):
    try:
        return d[key]
    except KeyError:
        print("key not found")
    except Exception as e:
        print(f"an error occurred: {e}")


get_key({"name": "Alice"}, "age") # key not found

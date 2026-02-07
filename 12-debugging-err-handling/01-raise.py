# raise your own exceptions
# - in python you can raise your own exceptions using the raise keyword
# - you can raise built-in exceptions or create your own custom exceptions

# raise a built-in exception
# raise ValueError("This is a value error")
def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

def colorize(text, color):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    if color not in colors:
        raise ValueError("invalid color")
    
    return f"{color}: {text}"
                                                 
def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


PI = 3.14159


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("cannot divide by zero")
    except TypeError:
        raise TypeError("both arguments must be numbers")
    except Exception as e:
        raise Exception(f"an error occurred: {e}")


def colorize(text, color):
    colors = ('red', 'green', 'blue')

    try:
        if type(text) is not str:
            raise TypeError("text must be a string")

        if color not in colors:
            raise ValueError("invalid color")

        return f"{color}: {text}"
    except TypeError as e:
        raise TypeError(e)
    except ValueError as e:
        raise ValueError(e)


def say_hi():
    print(f"Hi from {__name__}")


if __name__ == "__main__":
    say_hi()

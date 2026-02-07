# extermal modules
# - external modules are modules that are not part of the Python standard library, but can be installed and used in your code
# - you can install external modules using pip, the Python package manager
# - once you have installed an external module, you can import it and use its functions, classes, and variables in your code

from termcolor import colored
from pyfiglet import figlet_format

print(colored("Hello, World!", "red"))  # prints "Hello, World!" in red
# prints "Hello, World!" in cyan with a green background
print(colored("Hello, World!", "cyan", "on_green"))
# prints "Hello, World!" in yellow with bold and underline attributes
print(colored("Hello, World!", "yellow", attrs=["bold", "underline"]))

# ascii art
# - ascii art is a technique that uses characters to create images and designs
# - the pyfiglet module is a popular library for creating ascii art in Python
valid_colors = ('red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 'white')


def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be a string")

    if color not in valid_colors:
        raise ValueError("invalid color")

    ascii_art = figlet_format(text)
    return colored(ascii_art, color=color)


def main():
    msg = input("what would you like to print? ")
    color = input("what color? ").lower()

    try:
        ascii_art = colorize(msg, color)
        print(ascii_art)
    except ValueError as e:
        print(e)
        print("defaulting to magenta")
        ascii_art = colorize(msg, "magenta")
        print(ascii_art)
    except TypeError as e:
        print(e)
        print("defaulting to magenta")
        ascii_art = colorize(str(msg), "magenta")
        print(ascii_art)


if __name__ == "__main__":
    main()
    color = "magenta"

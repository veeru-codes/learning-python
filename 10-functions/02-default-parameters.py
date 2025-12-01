# why have default parameters?
# - allows you to be more defensive
# - avoids errors with incorrect parameters
# - more readable examples

# what can default parameters be?
# - anything! functions, lists, dictionaries, strings, booleans - all of the above!
def exponent(num, power=2):
    return num ** power


print(exponent(5, 2))  # 25
print(exponent(3, 2))  # 9
print(exponent(2))  # 4


def show_information(first_name="veerendranath", is_instructor=False):
    if first_name == "veerendranath" and is_instructor:
        return "welcome back instructor veerendranath!"
    elif first_name == "veerendranath":
        return "i really thought you were an instructor..."

    return f"hello {first_name}"


print(show_information())  # "I really thought you were an instructor..."
print(show_information(is_instructor=True))  # "welcome back instructor veerendranath!"
print(show_information(first_name="molly"))  # "hello molly!"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def math(a, b, fn=add):
    return fn(a, b)


print(math(2, 2))  # 4
print(math(2, 2, fn=subtract))  # 0

# default params should be at the end or need to assign default values to every params

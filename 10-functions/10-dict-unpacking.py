def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": 'colt', "second": 'jack'}
# display_names(names)
display_names(**names)


def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("other stuff...")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name="tony")
add_and_multiply_numbers(**data)

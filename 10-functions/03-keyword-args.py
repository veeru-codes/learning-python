# why use keyword arguments?
# - it's useful when passing a dictionary to a function and
# - unpacking its values
# - a little more flexibility

# different from default parameters?
# - when you define a function and use an = you are setting a default parameter
# - when you invoke a function and use an = you are making a keyword argument

def full_name(first_name, last_name):
    return f'{first_name} {last_name}'


full_name('john', 'smith')  # john smith
full_name(first_name='john', last_name='smith')  # john smith
full_name(last_name='smith', first_name='john')  # john smith

# a variable in python is like a variable in mathematics: it is a named symbol that holds a value
# variables are always assigned with the variable name on the left and the value on the right of the equals sign
# variables must be assigned before they can be used

x = 100
khaleesi_mother_of_dragons = 10
print(x + khaleesi_mother_of_dragons) # 110

# variables can be:
# - assigned to other variables
# - reassigned at any time
# - assigned at the same time as other variables

python_is_awesome = 100
just_another_variable = python_is_awesome
python_is_awesome = 1337
five, ten, fifteen = 5, 10, 15

# naming restrictions
# - variables must start with a letter or underscore
# - the rest of the name must consist of letters, numbers, or underscores
# - names are case-sensitive

# naming conventions
# - most variables should be snake_case (underscores between words)
# - most variables should also be lowercase
#   - constants in UPPERCASE
#   - class names in UpperCamelCase
# - variables that start and end with two underscores (called dunder for double underscore) are
# - supposed to be private or left alone: __no_touchy__
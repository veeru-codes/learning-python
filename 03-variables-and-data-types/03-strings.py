# string literals in python can be declared with either single or double quotes
# either one is perfectly fine; but make sure you stick to the same convention throughout the same file

name1 = 'veerendranath'
name2 = 'pranava'
msg = "he said 'hello there'"

# concatenation is combining multiple strings together.
# in python, you can do this simply with the '+' operator

username = 'veerendranath'
print("hello there and welcome to the game, " + username + "!")

# there are also several ways to format strings in python to interpolate variables
# the new way is f-strings

guess = 8
print(f"your guess of {guess} is incorrect!")
name = "blue the cat"
print(f"your name is {name}")

# accessing the characters of a string
# strings are zero indexed
user = 'veerendranath'
print(user[0]) # 'v'
print(user[-1]) # 'h'


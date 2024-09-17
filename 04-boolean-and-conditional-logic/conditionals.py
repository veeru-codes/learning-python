from random import randint, choice

# if... elif... else...
name = "Arya Stark"

if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on")


# Coding exercise: Check if num is 7 or not
num = randint(1, 10)

if num == 7:
    print("lucky")
else:
    print("unlucky")

# Coding exercise: Check if num is even or odd
n = randint(1, 1000)

if n % 2 == 0:
    print("even")
else:
    print("odd")

# Multiple Elifs
color = input("What's your favorite color? ")
if color == 'purple':
    print("Excellent choice!")
elif color == 'teal':
    print("npt bad!")
elif color == 'seafoam':
    print("mediocre")
elif color == 'pure darkness':
    print("I like how you think")
else:
    print("You Monster!")

age = 6

# Conditional and Logical operators
if age > 1 and age < 8:
    print("You charge child amount")
else:
    print("You charge adult amount")

city = input("Where do you live? ")
if city == "los angeles" or city == "san fansisco":
    print("YOU LIVE IN CALIFORNIA")
else:
    print("YOU LIVE IN SOMEWHERE ELSE")

# Coding exercise: Food classifying
food = choice(['apple', 'grape', 'steak', 'bacon', 'worm', 'dirt'])
if food == "apple" or food == "grape":
    print("fruit")
elif food == "steak" or food == "bacon":
    print("meat")
elif food == "worm" or food == "dirt":
    print("yuck")


# age 2 - 8: 2 dollar ticket
# age 65 and more: 5 dollar ticket
# 10 dollars for everyone else

person_age = 21

if not ((person_age >= 2 and person_age <= 8) or person_age >= 65):
    print('YOU PAY 10 DOLLARS AND ARE NOT A CHILD OR SENIOR!')
else:
    print('YOU ARE A CHILD OR SENIOR!')

# is vs ==
a = 1
a == 1       # True
a is 1       # True

a = [1, 2, 3]
b = [1, 2, 3]
a == b       # True
a is b       # False

clone = b
b is clone   # True
# a process for executing a task
# it can accept input and return an output
# useful for executing similar procedures over and over
# why use functions?
# - stay DRY - don't repeat yourself
# - clean up and prevent code duplication
# - "abstract away" code for other users

from random import random


def sing_happy_birthday(name):
    print('happy birthday to you')
    print('happy birthday to you')
    print(f'happy birthday dear {name}')
    print('happy birthday to you')


# return
# - it exits the function
# - outputs whatever value is placed after the return keyword
# - pops the function off the call stack

def print_square_of_7():
    return 7 * 7


sing_happy_birthday('colt')
result = print_square_of_7()
print(result)


def coin_flip():
    random_number = random()
    if random_number > 0.5:
        return 'heads'
    else:
        return 'tails'


print(coin_flip())


def square(num):
    return num * num


def add(a, b):
    return a + b


print(square(5))
print(add(1, 2))

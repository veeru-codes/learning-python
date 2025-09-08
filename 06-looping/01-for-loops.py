# for loops
# in python, for loops are written like this:
# for item in iterable_object:
#   do something with item

# an iterable object is some kind of collection of items, for instance: a list of numbers, a string of character, a range etc.
# item is a new variable that can be called whatever you want
# item references the current position of your iterator within the iterable.
# it will iterate over every item of the collection and then go away when it has visited all items

for x in range(1, 10):
    print(x)

for char in 'coffee':
    print(char)

# ranges
# - range(endpoint) --> gives you integers from 0 to endpoint (exclusive)
# - range(start, endpoint) --> will give you integers from start to endpoint (exclusive)
# - range(start, endpoint, skip) --> will give you integers from start to endpoint by skipping
# - range(start, endpoint, -1) --> will give you integers in reverse order

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(10, 1, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2]


num = int(input('how many times do i have to tell you? '))

for i in range(num):
    print('clean up your room!')

for x in range(1, 21):
    if x == 4 or x == 13:
        print(f'{x} is unlucky')
    elif x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')

emoji = '😎'
for i in range(1, 10):
    print(emoji * i)


times = int(input('how many times do i have to tell you? '))
for i in range(times):
    print('clean up your room!')
    if i >= 4:
        print('do you even listen anymore?')
        break

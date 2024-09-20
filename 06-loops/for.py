for x in range(1, 10):
    print(f"{x} square is {x * x}")

for letter in 'coffee':
    print(letter)

# Exploring range
print(list(range(10)))
print(list(range(1, 10)))
print(list(range(0, 10, 2)))
print(list(range(10, 0, -2)))

# Coding exercise: Add up every odd number from 10 to 20
x = 0
for num in range(11, 21, 2):
    x += num

print("Sum of odd numbers between 10 and 20: ", x)

# Coding exercise: Repeater
num_times = int(input('How many times do I have to tell you? '))

for num in range(num_times):
    print('Clean Up Your Room!')

# Coding exercise: Unlucky numbers
for num in range(1, 20):
    if num == 4 or num == 13:
        print(f'{num} is UNLUCKY')
    elif num % 2 == 0:
        print(f'{num} is Even')
    else:
        print(f'{num} is Odd')
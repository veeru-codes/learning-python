for i in range(1, 100):
    if i % 10 == 0:
        print(i)

# Check if any even numbers are available in a list

myList = [1, 2, 3, 5, 7]

# In a for...else loop, the else block runs only
# if there isn't any break happens
for num in myList:
    if num % 2 == 0:
        print("Even number exists")
        break
else:
    print("Even numbers do not exists")

# Finding Prime Numbers
for num in range(2, 100):
    for factor in range(2, int(num**0.5) + 1):
        if num % factor == 0:
            break
    else:
        print(f"{num} is prime!")

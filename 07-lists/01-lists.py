# it's just a collection or grouping of items
# fundamental data structure for organizing data

tasks = ['install python', 'learn python', 'take a break']
print(tasks)
print(f'you have {len(tasks)} tasks to do...')

# accessing values in a list
# lists always start counting at zero. so first element lives at index 0
# you can use a negative number to index backwards

print(tasks[0]) # 'install python'
print(tasks[1]) # 'learn python'
print(tasks[2]) # 'take a break'
print(tasks[-1]) # 'take a break'

# check if a value is 'in' a list
print('install python' in tasks) # True

# iterating over lists
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number * number)

colors = ['red', 'blue', 'green', 'yellow', 'pink']
index = 0
while index < len(colors):
    print(f'{index}: {colors[index]}')
    index += 1



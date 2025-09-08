# we can also iterate using while loop, which has a different format
# while im_tired:
#   seek caffeine

# while loops continue to execute while a certain condition is truthy, and will end when they become falsy
# while loops require more careful setup than for loops, since you have to specify the termination conditions manually
# be careful! if the condition doesn't become false at some point, your loop will continue forever!

msg = input("what's your secret message? ")
while msg != 'bananas':
    print('wrong!')
    msg = input("what's your secret message? ")
print('correct!')

num = 1
while num <= 20:
    print(num)
    num += 1

for i in range(1, 10):
    emoji = ''
    count = 1
    while count <= i:
        emoji += '😎'
        count += 1
    print(emoji)


# controlled exit
# the keyword break gives us the ability to exit out of while loops whenever we want
# we can also use it to end for loops early



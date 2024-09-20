msg = input("What's the secret password? ")

while msg != 'bananas':
    print('Wrong!')
    msg = input("What's the secret password? ")

print("Correct!")

num = 1

while num < 10:
    print(f"num is {num}")
    num += 1

# Coding exercise: Emoji art
for num in range(10):
    print("😄" * num)

i = 1

while i < 10:
    print("😄" * i)
    i += 1
    
# Coding exercise: Stop copying me
msg = input('Say something: ')

while msg != 'stop copying me':
    print(msg)
    msg = input()

print('Okay You Win!')
for i in range(100):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

n1 = 2
n2 = 4
n3 = 8

greater = n1 if (n1 > n2) and (n1 > n3) else n2 if (n2 > n1) and (n2 > n3) else n3
print(greater)

n = 1

# If n is even then it will continue to next iteration
# else print n
while n <= 10:
    if n % 2 == 0:
        n += 1
        continue

    print(n)
    n += 1

m = 1

# If m is 5 then the loop will be terminated
while m <= 10:
    if m == 5:
        print("breaking out of the loop as m is 5")
        break

    print(m)
    m += 1

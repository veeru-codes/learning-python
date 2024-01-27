def collectPrimes(num):
    primes = [2]
    for number in range(2, num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor == 0:
                break
            if factor > sqrtNum:
                primes.append(number)
                break

    return primes


collectPrimes(10)

# Finding Prime Numbers
for num in range(2, 100):
    for factor in range(2, int(num**0.5) + 1):
        if num % factor == 0:
            break
    else:
        print(f"{num} is prime!")

primes = [2, 3, 5, 7]

def is_prime(num):
    for j in primes:
        if num % j == 0:
            return False
    return True

nprime = 10001
i = 9
while len(primes) < nprime:
    if is_prime(i):
        primes.append(i)
    i += 2

print(primes[nprime - 1])

def largest_prime(num):
    ans, div = num, 1
    while div < ans**(1/2.0):
        if ans % div == 0:
            ans /= div
        div += 1
    return ans

num = 600851475143
print(int(largest_prime(num)))

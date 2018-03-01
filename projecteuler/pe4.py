num1 = 999
num2 = 999


def is_palindrome(numstr):
    if len(numstr) <= 1:
        return True
    if numstr[0] != numstr[-1]:
        return False
    return is_palindrome(numstr[1:-1])

palindromes = []

for i in range(num1, 100, -1):
    for j in range(num2, 100, -1):
        num = i * j
        if is_palindrome(str(num)):
            palindromes.append(num)

print(sorted(palindromes)[-1])

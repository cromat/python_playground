i = 1
j = 2
sum_even = 0
while i < 4000000:
    if i % 2 == 0:
        sum_even += i
    if j % 2 == 0:
        sum_even += j
    i = i + j
    j = j + i

print(sum_even)

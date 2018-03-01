# First way
sum_sqr = 0
sqr_of_sum = 0

for i in range(1, 101):
    sum_sqr += i ** 2
    sqr_of_sum += i

sqr_of_sum **= 2

print(sqr_of_sum - sum_sqr)

# Second way
r = range(1, 101)
print(sum(r) ** 2 - sum([x ** 2 for x in r]))

from time import time

def timer(func):
    def f(x, y):
        before = time()
        res = func(x, y)
        after = time()
        print('Elapsed time: ' + str(after - before))
        return res
    return f

@timer
def add(x, y):
    return x + y

@timer
def sub(x, y):
    return x - y

print(add(4,5))

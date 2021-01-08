from functools import lru_cache

@lru_cache(maxsize = 100)
def fibonacci(n):
    if type(n) != int:
        raise TypeError('Input must be a positive integer')
    elif n < 1:
        raise ValueError('Input must be a positive integer')
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(-3))
print(fibonacci('3'))

fib_cache = {}
def fibonacci_check(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_check(n - 1) + fibonacci_check(n - 2)
    fib_cache[n] = value
    return value

print(fibonacci_check(50))
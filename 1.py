import timeit
from functools import lru_cache


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(None)
def factorial_recursive_with_lru_cache(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


@lru_cache(None)
def fib_recursive_with_lru_cache(n):
    if n == 0 or n == 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == "__main__":
    print("Factorial Iterative:", timeit.timeit(lambda: factorial_iterative(10), number=100000))
    print("Fibonacci Iterative:", timeit.timeit(lambda: fib_iterative(10), number=100000))

    print("Factorial Recursive:", timeit.timeit(lambda: factorial_recursive(10), number=1000))
    print("Fibonacci Recursive:", timeit.timeit(lambda: fib_recursive(10), number=1000))

    print("Factorial Recursive with lru_cache:",
          timeit.timeit(lambda: factorial_recursive_with_lru_cache(10), number=1000))
    print("Fibonacci Recursive with lru_cache:", timeit.timeit(lambda: fib_recursive_with_lru_cache(10), number=1000))

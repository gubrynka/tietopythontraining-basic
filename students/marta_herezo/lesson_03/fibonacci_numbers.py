# Given a non-negative integer n,//
# print the nth Fibonacci number.


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("Give n: "))

print(fib(n))
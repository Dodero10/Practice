import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def approx_sin(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * (x ** (2 * i)) / factorial(2 * i)
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)
    return result
# Write a python program to calculate factorial of a number using reduce function
from functools import reduce

def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

num = int(input("Enter a number to find factorial: "))
print(factorial(num))
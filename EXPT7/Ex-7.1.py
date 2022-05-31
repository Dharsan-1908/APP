from functools import reduce


def fib(n): return reduce(lambda x, _: x+[x[-1]+x[-2]],
                          range(n-2), [0, 1])


print(fib(5))

# map and lambda method

# def fib(n):
    # fiblist = [0,1]

    # any(map(lambda _:fiblist.append(sum(fiblist[-2:])),range(2, n)))
    # return fiblist[:n]

# print(fib(15))
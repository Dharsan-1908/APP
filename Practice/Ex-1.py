list = [1, 2, 6, 3, 7, 34, 7, 8, 234, 5, 1, 88, 7,
        87, 34, 12, 31, 123, 9, 7, 7, 7, 23, 432, 4, ]


def even(n):
    for x in n:
        if(x % 2 == 0):
            print(x)


def odd(n):
    for x in n:
        if(x % 2 != 0):
            print(x)


even(list)
print("Odd")
odd(list)

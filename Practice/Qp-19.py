# Write a function that accepts a list
# find square and cube of each number in the list

list1 = [1, 234, 6, 36, 72, 7, 9, 8, 6, 12, 3]


def square(n):
    return list(map(lambda x: x*x, n))


def cube(n):
    return list(map(lambda x: x*x*x, n))


print(square(list1))
print(cube(list1))

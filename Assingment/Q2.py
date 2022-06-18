# write a python program to find the sum of all the elements of a list using reduce function
from functools import reduce
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sumList = reduce(lambda x, y: x + y, numList)
maxList = reduce(max, numList)

print("Sum of all the elements of a list: ", sumList)
print("Max of all the elements of a list: ", maxList)

row1 = int(input("row number"))
column1 = int(input("no of columns"))
arr = [[0 for col in range(column1)] for row in range(row1)]
for row in range(row1):
    for col in range(column1):
        arr[row][col] = row*col
print(arr)
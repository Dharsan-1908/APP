n = int(input("Enter the list size: "))
list1 = []
list2 = []
print("\nEnter list one value: ")

for i in range(0, n):
    num = input()
    list1.append(int(num))

print("\nEnter list two value: ")
for i in range(0, n):
    num = input()
    list2.append(int(num))

addList = list(map(lambda x, y: x+y, list1, list2))
subList = list(map(lambda x, y: x-y, list1, list2))

print("Addition of two list: \n")
print(addList)
print("Difference between two list \n")
print(subList)

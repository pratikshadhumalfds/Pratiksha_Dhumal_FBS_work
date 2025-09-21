###Python Program to Sort the List According to the Second Element in Sublist.

##with build-in fun
data = [[1, 5], [3, 2], [4, 8], [2, 4]]
sorted_data = sorted(data, key=lambda x: x[1])

print("Sorted list by second element:", sorted_data)


#without build-in function.
data = [[1, 5], [3, 2], [4, 8], [2, 4]]

n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][1] > data[j + 1][1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

print("Sorted list by second element:", data)

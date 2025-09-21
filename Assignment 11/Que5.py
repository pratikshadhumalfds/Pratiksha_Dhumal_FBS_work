###Python Program to Sort a List According to the Length of the Elements within the list.

#bulid-in function used.
data = ["apple", "banana", "kiwi", "fig", "pineapple"]

data.sort(key=len)
print("Sorted list by length:", data)

#without build-in function.
data = ["apple", "banana", "kiwi", "fig", "pineapple"]
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(data[j]) > len(data[j + 1]):
            # Swap
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp
print("Sorted list by length:", data)

###Python Program to Find the Second Largest Number in a List Using Bubble Sort

numbers = [12, 45, 23, 67, 34, 89, 10]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

second_largest = numbers[-2]

print("Sorted List:", numbers)
print("Second Largest Number:", second_largest)

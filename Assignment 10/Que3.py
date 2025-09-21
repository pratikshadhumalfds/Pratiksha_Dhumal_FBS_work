##Write a program to find the second largest element in the list...

#without build-in function.
numbers = [10, 67, 30, 55, 11, 70]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest element not found.")
else:
    print("Second largest element is:", second_largest)

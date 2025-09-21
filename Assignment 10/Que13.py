###Write a program to print list after removing even numbers.

#with build-in function
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 17, 19]

odd_numbers = [num for num in numbers if num % 2 != 0]

print("List after removing even numbers:", odd_numbers)


#without build-in function.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 17, 19]

odd_numbers = [0] * len(numbers)
index = 0

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        odd_numbers[index] = numbers[i]
        index += 1

print("Odd numbers:", end=" ")
for i in range(index):
    print(odd_numbers[i], end=" ")
print()

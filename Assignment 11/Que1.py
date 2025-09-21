###Python Program to Put Even and Odd elements of a List into two Different Lists

#with build-in function.
numbers = [12, 7, 9, 14, 5, 20, 3, 8]

even_list = [x for x in numbers if x % 2 == 0]
odd_list = [x for x in numbers if x % 2 != 0]

print("Original List:", numbers)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)



#without build-in function.
numbers = [12, 7, 9, 14, 5, 20, 3, 8]

even_list = [0] * len(numbers)
odd_list = [0] * len(numbers)

even_index = 0
odd_index = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_list[even_index] = numbers[i]
        even_index += 1
    else:
        odd_list[odd_index] = numbers[i]
        odd_index += 1

print("Original List:", numbers)

print("Even Numbers:", end=" ")
for i in range(even_index):
    print(even_list[i], end=" ")
print()

print("Odd Numbers:", end=" ")
for i in range(odd_index):
    print(odd_list[i], end=" ")
print()


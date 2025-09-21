###Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have even elements
# and other will have odd elements.

#with build-in function
n = int(input("Enter number of elements: "))

original_list = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    original_list.append(num)

even_list = [x for x in original_list if x % 2 == 0]
odd_list = [x for x in original_list if x % 2 != 0]

print("Original List:", original_list)
print("Even Elements:", even_list)
print("Odd Elements:", odd_list)



###without build-in function
n = int(input("Enter number of elements: "))

original_list = [0] * n

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    original_list[i] = num

even_list = [0] * n
odd_list = [0] * n

even_index = 0
odd_index = 0

for i in range(n):
    if original_list[i] % 2 == 0:
        even_list[even_index] = original_list[i]
        even_index += 1
    else:
        odd_list[odd_index] = original_list[i]
        odd_index += 1

print("Original List:", original_list)

print("Even Elements:", end=" ")
for i in range(even_index):
    print(even_list[i], end=" ")
print()

print("Odd Elements:", end=" ")
for i in range(odd_index):
    print(odd_list[i], end=" ")
print()

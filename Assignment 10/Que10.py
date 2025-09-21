###Write a program to remove all occurrences of a given element in the list.

###with using build-in function.
n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

target = int(input("Enter element to remove: "))
new_list = [num for num in lst if num != target]

print("Original list:", lst)
print(f"List after removing all occurrences of {target}:", new_list)



###without build-in function
n = int(input("Enter number of elements: "))

list = [0] * n
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    list[i] = num

target = int(input("Enter element to remove: "))

filtered_list = [0] * n  
index = 0  

for i in range(n):
    if list[i] != target:
        filtered_list[index] = lst[i]
        index += 1

print("Original list:", lst)
print(f"List after removing all occurrences of {target}:", end=" ")
for i in range(index):
    print(filtered_list[i], end=" ")
print()


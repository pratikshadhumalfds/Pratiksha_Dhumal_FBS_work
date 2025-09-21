###Python Program to Merge Two Lists and Sort it

#using build-in function
list1 = [5, 2, 9, 1]
list2 = [8, 3, 7, 4]
merged_list = list1 + list2
merged_list.sort()
print("Merged and Sorted List:", merged_list)



#without build-in function
list1 = [5, 2, 9, 1]
list2 = [8, 3, 7, 4]

merged_size = len(list1) + len(list2)
merged_list = [0] * merged_size 

for i in range(len(list1)):
    merged_list[i] = list1[i]

for j in range(len(list2)):
    merged_list[len(list1) + j] = list2[j]

for i in range(merged_size):
    for j in range(0, merged_size - i - 1):
        if merged_list[j] > merged_list[j + 1]:
            temp = merged_list[j]
            merged_list[j] = merged_list[j + 1]
            merged_list[j + 1] = temp

print("Merged and Sorted List:", end=" ")
for i in range(merged_size):
    print(merged_list[i], end=" ")
print()
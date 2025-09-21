###Write a program to remove duplicates from the list.

###with build-in function
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_list = list(set(my_list))

print("List without duplicates:", unique_list)

###without build-in function
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]

unique_list = []

for item in my_list:
    already_exists = False
    for unique_item in unique_list:
        if item == unique_item:
            already_exists = True
            break
    if not already_exists:
        unique_list.append(item)

print("List without duplicates:", unique_list)


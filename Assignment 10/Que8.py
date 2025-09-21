###Write a program to create a duplicate of an existing list. It should not point to same list...

#with build-in function.
original_list = [1, 2, 3, 4, 5]

copied_list = original_list[:]

print("Original List:", original_list)
print("Copied List:  ", copied_list)

print("###################################")

###without build-in function.
original_list = [1, 2, 3, 4, 5]

copied_list = []

for item in original_list:
    copied_list += [item]  # Using + to avoid append()

print("Original List:", original_list)
print("Copied List:  ", copied_list)


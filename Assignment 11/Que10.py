###Write a program to print list after removing even numbers.

#Using built-in function
def remove_even_numbers(lst):
    return [x for x in lst if x % 2 != 0]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_even_numbers(original_list)

print("Original List:", original_list)
print("After Removing Even Numbers:", filtered_list)


#without build-in function
def remove_even_numbers_no_builtin(lst):
    result = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            result.append(lst[i])
        i += 1
    return result

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_even_numbers_no_builtin(original_list)

print("Original List:", original_list)
print("After Removing Even Numbers:", filtered_list)


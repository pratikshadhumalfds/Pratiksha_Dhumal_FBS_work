####Python Program to Find the Union of two Lists.

#build-in function.
def union_with_builtin(list1, list2):
    return list(set(list1) | set(list2)) 

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = union_with_builtin(list1, list2)
print("Union using built-in:", result)



#without build-in function.
def union_without_builtin(list1, list2):
    union = []

    for item in list1:
        if item not in union:
            union.append(item)
    
    for item in list2:
        if item not in union:
            union.append(item)

    return union

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = union_without_builtin(list1, list2)
print("Union without built-in:", result)


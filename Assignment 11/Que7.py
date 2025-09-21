###Python Program to Find the Intersection of Two Lists.


#using build-in function
def intersection_lists(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection of two lists:", intersection_lists(list1, list2))


# Without using built-in set function
def intersection_lists(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection of two lists:", intersection_lists(list1, list2))

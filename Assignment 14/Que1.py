###Write a Python program to find elements in a given set that are not in another set.

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

difference = set_a - set_b

print("Elements in set_a but not in set_b:", difference)

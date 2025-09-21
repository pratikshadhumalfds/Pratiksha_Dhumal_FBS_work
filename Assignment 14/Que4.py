###Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

numbers = [1, 5, 7, -1, 5]
given_value = 6

print(f"Pairs with sum {given_value}:")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == given_value:
            print(f"({numbers[i]}, {numbers[j]})")

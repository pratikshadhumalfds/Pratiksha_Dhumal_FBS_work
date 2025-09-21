#Write a program to find maximum and minimum element in a list.

#Without using built-in function.
numbers = [10, 70, 33, 26, 10, 85]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum element is:", maximum)
print("Minimum element is:", minimum)



#with using build in function.
numbers = [56, 45, 28, 11, 90, 48]

maximum = max(numbers)
minimum = min(numbers)

print("Maximum element is:", maximum)
print("Minimum element is:", minimum)


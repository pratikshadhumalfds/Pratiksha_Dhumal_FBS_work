#Write a program to find sum of all elements of list....

#with using build-in function.
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("The sum of all elements in the list is:", total)

# Without using built-in function.  
numbers = [100, 487, 234, 345]

total = 0

for num in numbers:
    total += num

print("The sum of all elements in the list is:", total)



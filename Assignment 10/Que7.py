###Write a program to create a new list from existing list which contains cube of each number of list...

###with build-in function.
numbers = [1, 2, 3, 4, 5]
cubes = []

for num in numbers:
    cubes.append(num ** 3)

print("Cubes of the list:", cubes)

###without build-in function.
numbers = [1, 2, 3, 4, 5]

length = 0
for _ in numbers:
    length += 1

cubes = [0] * length
index = 0
for num in numbers:
    cubes[index] = num * num * num 
    index += 1
print("Cubes of the list:", cubes)






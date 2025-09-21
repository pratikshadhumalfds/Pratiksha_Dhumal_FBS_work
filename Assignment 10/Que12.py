

#with build-in function.
n = int(input("Enter number of elements: "))

numbers = []
squares = []
cubes = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    squares.append(num ** 2)
    cubes.append(num ** 3)

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)

###without build-in function.
n = int(input("Enter number of elements: "))

numbers = [0] * n
squares = [0] * n
cubes = [0] * n

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers[i] = num
    squares[i] = num * num
    cubes[i] = num * num * num

print("Numbers:", end=" ")
for i in range(n):
    print(numbers[i], end=" ")
print()

print("Squares:", end=" ")
for i in range(n):
    print(squares[i], end=" ")
print()

print("Cubes:", end=" ")
for i in range(n):
    print(cubes[i], end=" ")
print()


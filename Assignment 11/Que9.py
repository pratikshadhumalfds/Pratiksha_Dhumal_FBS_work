###Write a program to create three lists of numbers, their squares and cubes.

#using built-in functions
def create_lists(n):
    numbers = list(range(1, n + 1))
    squares = [x ** 2 for x in numbers]
    cubes = [x ** 3 for x in numbers]

    return numbers, squares, cubes

n = 10
numbers, squares, cubes = create_lists(n)

print("Number | Square | Cube")
print("-----------------------")
for i in range(n):
    print(f"{numbers[i]:6} | {squares[i]:6} | {cubes[i]:4}")



#using without build-in function.
def create_lists_no_builtin(n):
    numbers = []
    squares = []
    cubes = []

    i = 1
    while i <= n:
        numbers.append(i)
        squares.append(i * i)
        cubes.append(i * i * i)
        i += 1

    return numbers, squares, cubes

n = 10
numbers, squares, cubes = create_lists_no_builtin(n)

print("Number | Square | Cube")
print("-----------------------")
i = 0
while i < n:
    print(f"{numbers[i]:6} | {squares[i]:6} | {cubes[i]:4}")
    i += 1



##Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers,
#adding up to a target number.

numbers = [1, 2, 3, 4, 5, 6]
target = 10

result = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                triplet = sorted([numbers[i], numbers[j], numbers[k]])
                if triplet not in result:
                    result.append(triplet)

print("Unique triplets that sum to", target)
for triplet in result:
    print(triplet)

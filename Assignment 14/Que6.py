##Write a Python program to find the two numbers whose product is
#maximum among all the pairs in a given list of numbers. Use the Python set.

numbers = [1, 10, -5, 4, -6]

numbers = list(set(numbers))

max_product = float('-inf')
num1, num2 = 0, 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]
        if product > max_product:
            max_product = product
            num1, num2 = numbers[i], numbers[j]

print("Max product is", max_product)
print("Numbers are:", num1, "and", num2)

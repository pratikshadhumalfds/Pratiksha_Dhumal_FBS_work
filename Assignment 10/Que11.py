###Write a program to print all numbers which are divisible by m and n in the list.


list = [12, 24, 108, 36, 60, 72]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

result = [num for num in list if num % m == 0 and num % n == 0]

print(f"Numbers divisible by both {m} and {n}:", result)



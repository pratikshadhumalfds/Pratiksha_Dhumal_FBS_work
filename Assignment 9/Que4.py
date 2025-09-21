#Write a program to find sum of n numbers using recursion.

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

n = int(input("Enter a number: "))
if n < 0:
    print("Please enter a non-negative number.")
else:
    total = sum(n)
    print(f"Sum of first {n} numbers is: {total}")

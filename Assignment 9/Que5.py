# Write a program to find factorial using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a Number:"))
if num < 0:
    print("Factorial is  not defined for Negative Numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")    

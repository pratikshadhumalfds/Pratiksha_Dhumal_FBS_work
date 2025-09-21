#Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!

n = 10
def factorial(n):  #recursive fun to cal fact.
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_of_factorials(n):       #recursive fun to cal sum of facts from 1 to n
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_of_factorials(n - 1)

result = sum_of_factorials(n)
print(f"The sum of factorials from 1! to {n}! is:", result)

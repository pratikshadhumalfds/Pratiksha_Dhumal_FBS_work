#Write a program to check if given number is Armstrong or not using recursive function.

def armstrong_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return(digit ** power) + armstrong_sum(num // 10, power)

n = int(input("Enter a Number:"))
num_digits = len(str(n))
result = armstrong_sum(n, num_digits)
if result == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not Armstrong number.")    



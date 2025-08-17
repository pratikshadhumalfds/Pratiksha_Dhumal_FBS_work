def sum_digits(num):
    s=0
    while num > 0:
        s+= num % 10
        num //= 10
        return s
n=int(input("Enter the number:"))
print('Sum of digits',sum_digits(n))
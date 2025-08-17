def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num //=10
    return rev

n=int(input("Enter the number:"))
print('Reverse number:', reverse_number(n))    
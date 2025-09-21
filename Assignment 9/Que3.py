#Write a program to reverse a given number using recursive function....

num = 1234567
def reverse_no(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_no(n // 10, rev)

reversed_num = reverse_no(num)
print(f"Reversed number: {reversed_num}")

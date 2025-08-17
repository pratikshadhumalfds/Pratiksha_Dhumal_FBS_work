def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num //=10
    return rev

def is_palindrome(num):
    return num == reverse_number(num)

num=int(input("Enter the number:"))
if is_palindrome(num):
    print(num,"Is a Palindrome number")
else:
    print(num,"Not a Palindrome")

 
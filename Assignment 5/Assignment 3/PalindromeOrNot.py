###WAP to check if given 3 digit number is a palindrome or not...

a1 = int(input("Enter the number:"))
a2 = int(input("Enter the number:"))
a3 = int(input("Enter the number:"))

ori_num = (a1 * 100) +(a2 * 10) + (a3)
rev_num = (a3 * 100) +(a2 * 10) + (a1)

if (rev_num == ori_num):
    print(f'{ori_num} is a Palindrome number')
else:
    print(f'{ori_num} is not a Palindrome number')

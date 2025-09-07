###Python program to count number of digits and letters in a string..

str_with_digit = 'Hello world 1234567'

letter = 0
digit = 0

for char in str_with_digit:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        digit += 1

print('Number of letters:', letter)
print('Number of digits:', digit)

###python program to remove the characters of Odd index values in a string..

str = 'Hello World'
result = ' '
 
for char in range(len(str)):
    if char % 2 == 0:
        result += str[char]

print('Remove the characters of Odd index values in a string:', result)

